from sqlalchemy.orm import registry, relationship
from sqlalchemy import Table, MetaData, Column, String, Date, ForeignKey
from domain.model import Book, Member, Borrow


mapper_registry = registry()
metadata = MetaData()

books_table = Table(
    "books",
    metadata,
    Column("book_id", String, primary_key=True),
    Column("book_name", String, nullable=False),
)

members_table = Table(
    "members",
    metadata,
    Column("member_id", String, primary_key=True),
    Column("member_name", String, nullable=False),
)

borrows_table = Table(
    "borrows",
    metadata,
    Column("borrow_id", String,  primary_key=True),
    Column("borrower", String, ForeignKey("members.member_id"), nullable=False),
    Column("borrowed_book", String, ForeignKey("books.book_id"), nullable=False),
    Column("due_date", Date, nullable=False),
)


def start_mappers():
    """SQLAlchemy ORM ile Python nesnelerini tablolarla eşleştirir."""
    mapper_registry.map_imperatively(Book, books_table, properties={
        "borrowers": relationship(Borrow, backref="book")
    })
    mapper_registry.map_imperatively(Member, members_table, properties={
        "borrowed_books": relationship(Borrow, backref="member")
    })
    mapper_registry.map_imperatively(Borrow, borrows_table)
