import abc
from adapters.repository import BookRepository
from adapters.repository import MemberRepository
from database import SessionLocal


class AbstractUnitOfWork(abc.ABC):
    """Tüm UnitOfWork sınıfları için ortak bir şablon sağlar."""

    books: BookRepository
    members: MemberRepository

    # (1) Her UnitOfWork bir repository kullanmalı

    def __exit__(self, exc_type, exc_value, traceback):
        """Hata olup olmadığını kontrol et ve rollback'i sadece hata varsa yap."""
        if exc_type:
            self.rollback()


    @abc.abstractmethod
    def commit(self):
        """İşlemi tamamlar ve veritabanına kaydeder."""
        raise NotImplementedError  # (3)

    @abc.abstractmethod
    def rollback(self):
        """Yapılan değişiklikleri geri alır."""
        raise NotImplementedError  # (4)


class BookUnitOfWork(AbstractUnitOfWork):
    """Kitap işlemleri için Unit of Work yönetimi sağlar."""

    def __enter__(self):
        """With bloğuna girildiğinde session başlatır ve repository oluşturur."""
        self.session = SessionLocal()
        self.books = BookRepository(self.session)  # (1) Book Repository başlat
        return self

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def commit(self):
        """İşlemi tamamlar ve veritabanına kaydeder."""
        try:
            print("✅ COMMIT ÇAĞRILDI")  # Debugging
            self.session.commit()
            print("✅ COMMIT BAŞARILI")  # Commit başarılıysa yazdır
        except Exception as e:
            print(f"🚨 COMMIT HATASI: {e}")  # Eğer hata oluşursa, bunu görelim
            raise  # Hatanın detaylarını görmek için yeniden fırlat

    def rollback(self):
        """Yapılan değişiklikleri geri alır."""
        self.session.rollback()


class MemberUnitOfWork(AbstractUnitOfWork):
    """Üye işlemleri için Unit of Work yönetimi sağlar."""

    def __enter__(self):
        """With bloğuna girildiğinde session başlatır ve repository oluşturur."""
        self.session = SessionLocal()
        self.members = MemberRepository(self.session)  # (1) Member Repository başlat
        return self

    def __exit__(self, *args):
        """Üst sınıfın __exit__() metodunu çağır ve session'ı kapat."""
        super().__exit__(*args)
        self.session.close()  # (2) SQLAlchemy bağlantısını kapat

    def commit(self):
        """İşlemi tamamlar ve veritabanına kaydeder."""
        try:
            print("✅ COMMIT ÇAĞRILDI memberr")  # Debugging
            self.session.commit()
            print("✅ COMMIT BAŞARILI")  # Commit başarılıysa yazdır
        except Exception as e:
            print(f"🚨 COMMIT HATASI: {e}")  # Eğer hata oluşursa, bunu görelim
            raise  # Hatanın detaylarını görmek için yeniden fırlat

    def rollback(self):
        """Yapılan değişiklikleri geri alır."""
        self.session.rollback()