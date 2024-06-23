from sqlalchemy.orm import Session
import models, schemas


def get_author(db: Session, author_id: int):
    return db.query(models.Author).filter(
        models.Author.id == author_id
    ).first()


def get_author_by_name(db: Session, author_name: str):
    return db.query(models.Author).filter(
        models.Author.name == author_name
    ).first()


def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(**author.dict())
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author


def get_authors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Author).offset(skip).limit(limit).all()


def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Book).offset(skip).limit(limit).all()


def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def create_author_book(db: Session, book: schemas.BookCreate, author_id: int):
    db_book = models.Book(**book.dict(), author_id=author_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book
