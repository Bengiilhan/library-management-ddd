from typing import Callable, Dict, List, Type
from domain.model import BookBorrowedByMemberEvent


class MessageBus:
    HANDLERS: Dict[Type, List[Callable]] = {}

    @staticmethod
    def handle(event, buow):

        for handler in MessageBus.HANDLERS.get(type(event), []):
            try:
                handler(event, buow)
            except Exception as e:
                print(f"Error running handler: {e}")
                raise

    @staticmethod
    def issue_book_handler(event: BookBorrowedByMemberEvent, buow):
        with buow:
            book = buow.books.get(event.borrow.borrowed_book)
            if not book:
                return
            borrow = buow.session.merge(event.borrow)
            book.issue(borrow)
            print(book.borrowers[0].due_date)
            buow.commit()


MessageBus.HANDLERS = {
    BookBorrowedByMemberEvent: [MessageBus.issue_book_handler]
}
