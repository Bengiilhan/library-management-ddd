from domain.model import Book
from domain.model import Member
from datetime import date, timedelta


class DueDateCalculateService:
    @staticmethod
    def calculate(member: Member, book: Book) -> date:
        # Simple business rule: Every book purchased must be returned after 14 days
        return date.today() + timedelta(days=14)
