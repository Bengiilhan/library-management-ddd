from service_layer.due_date_calculator import DueDateCalculateService
from domain.model import Borrow
from service_layer.unit_of_work import MemberUnitOfWork
from service_layer.unit_of_work import BookUnitOfWork
from event_handlers.message_bus import MessageBus


def issue_book(book_id, member_id, muow: MemberUnitOfWork, buow: BookUnitOfWork):
    with muow, buow:
        member = muow.members.get(member_id)
        book = buow.books.get(book_id)

        # Due date hesapla
        due_date = DueDateCalculateService.calculate(member, book)
        borrow = Borrow(member_id, book_id, due_date)

        # Üyeye kitabı ödünç ver
        member.issue(borrow)

        # İşlemi kaydet
        muow.commit()

        # Üye olaylarını işle
        while member.events:
            event = member.events.pop(0)
            MessageBus.handle(event, buow)

