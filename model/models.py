from mysql_script.db_connect import db
from datetime import datetime
from sqlalchemy.orm import relationship

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255),  nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    
    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name

class Book(db.Model):
    __tablename__ = 'book'
    book_id = db.Column(db.Integer,  primary_key=True,
                   nullable=False, autoincrement=True)
    book_name = db.Column(db.String(255),nullable=False)
    publisher = db.Column(db.String(255),nullable=False)
    author = db.Column(db.String(255),nullable=False)
    publication_date = db.Column(db.Date, nullable = False)
    pages = db.Column(db.String(255), nullable = False)
    isbn = db.Column(db.String(255), nullable = False)
    description = db.Column(db.Text)
    link = db.Column(db.String(255))
    remaining = db.Column(db.Integer)
    rating = db.Column(db.Integer, default=5)

    def __init__(self, book_name, publisher, author):
        self.book_name = book_name
        self.publisher = publisher
        self.author = author



class BorrowBook(db.Model):
    __tablename__ = 'borrowbook'

    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    book_id = db.Column(db.Integer)
    email = db.Column(db.String(255))
    rental_date    = db.Column(db.Date, nullable=False)
    return_date    = db.Column(db.DateTime)

    def __init__(self, book_id, email, rental_date):
        self.book_id = book_id
        self.email = email
        self.rental_date = rental_date


class BookComment(db.Model):
    __tablename__ = 'bookcomment'
    id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    book_id = db.Column(db.Integer)
    email = db.Column(db.String(255),  nullable=False)
    content = db.Column(db.Text, nullable=False) 
    rating = db.Column(db.Integer)

    def __init__(self, book_id, email, content):
        self.book_id = book_id
        self.email = email
        self.content = content

# class Post(db.Model):
#     __tablename__ = 'post'
#     id = db.Column(db.Integer,  primary_key=True,
#                    nullable=False, autoincrement=True)
#     author = db.Column(db.String(256), nullable=False)
#     content = db.Column(db.Text(), nullable=False)
#     created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
#     def __init__(self, author,content):
#         self.author = author
#         self.content = content
