import abc
from domain.model import Book, BookId
from domain.model import Member, MemberId


class AbstractRepository(abc.ABC):
    """Tüm repository'ler için ortak bir şablon."""

    def __init__(self, session):
        self.session = session

    @abc.abstractmethod
    def add(self, entity):
        """Yeni bir varlığı veritabanına ekler."""
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, entity_id):
        """Bir varlığı ID'ye göre getirir."""
        raise NotImplementedError


class BookRepository(AbstractRepository):
    """Kitap işlemleri için SQLAlchemy repository."""

    def add(self, book: Book):
        """Yeni bir kitabı veritabanına ekler."""
        self.session.add(book)

    def get(self, book_id: BookId):
        """ID'ye göre kitabı getirir."""
        return self.session.query(Book).filter_by(book_id=book_id).one_or_none()

    def list(self):
        """Tüm kitapları getirir."""
        return self.session.query(Book).all()


class MemberRepository(AbstractRepository):
    """Üye işlemleri için SQLAlchemy repository."""

    def add(self, member: Member):
        """Yeni bir üyeyi veritabanına ekler."""
        self.session.add(member)

    def get(self, member_id: MemberId):
        """ID'ye göre üyeyi getirir."""
        return self.session.query(Member).filter_by(member_id=member_id).one_or_none()

    def list(self):
        """Tüm üyeleri getirir."""
        return self.session.query(Member).all()
