from dataclasses import dataclass
from datetime import date
from uuid import uuid4
from typing import List


@dataclass(frozen=True)
class BookId:
    value: str

    def __init__(self, value: str = None):
        object.__setattr__(self, 'value', value if value else str(uuid4()))

    def __str__(self):
        return self.value


@dataclass(frozen=True)
class MemberId:
    value: str

    def __init__(self, value: str = None):
        object.__setattr__(self, 'value', value if value else str(uuid4()))

    def __str__(self):
        return self.value


@dataclass(frozen=True)
class BorrowId:
    value: str

    def __init__(self, value: str = None):
        object.__setattr__(self, 'value', value if value else str(uuid4()))

    def __str__(self):
        return self.value


class Borrow:
    def __init__(self, borrower: MemberId, borrowed_book: BookId, due_date: date, borrow_id: BorrowId = None):
        self.borrow_id = borrow_id.value if borrow_id else str(uuid4())
        self.borrower = borrower
        self.borrowed_book = borrowed_book
        self.due_date = due_date

    def __repr__(self):
        return f"Borrow(id={self.borrow_id}, borrower={self.borrower}, borrowed_book={self.borrowed_book}, due_date={self.due_date})"


class Book:
    def __init__(self, book_id: BookId, book_name: str):
        self.book_id = book_id.value if book_id else str(uuid4())
        self.book_name = book_name
        self.borrowers: List[Borrow] = []

    def issue(self, borrow: Borrow):
        self.borrowers.append(borrow)


class Member:
    def __init__(self, member_id: MemberId, member_name: str):
        self.member_id = member_id.value if member_id else str(uuid4())
        self.member_name = member_name
        self.borrowed_books: List[Borrow] = []
        self.events = []

    def issue(self, borrow: Borrow):
        if not hasattr(self, 'events'):
            self.events = []
        self.borrowed_books.append(borrow)
        event = BookBorrowedByMemberEvent(borrow)
        self.events.append(event)


class BookBorrowedByMemberEvent:
    def __init__(self, borrow: Borrow):
        if not isinstance(borrow, Borrow):
            raise TypeError("Expected borrow to be an instance of Borrow")
        self.borrow = borrow


