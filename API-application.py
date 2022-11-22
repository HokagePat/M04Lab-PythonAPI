#Author: Patrick Szpak
#Date: 11/21/2022
#Program: CRUD API for books using Caleb Curry's demonstration from his video titled
# "REST API Crash Course - Introduction + Full Python API Tutorial"
#This program follows Caleb Curry's tutorial but switches the drinks and drink classifications with
#books and the book id, author, name, publisher. This would not have been possible without Caleb, so THANK YOU!

from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(80))


def __repr__(self):
    return f"{self.name} - {self.author}"


@app.route('/books')
def index():
    return 'Hello!'


@app.route('/books')
def get_books():
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {'id': book.id, 'name': book.name, 'author': book.author, 'publisher': book.publisher}

        output.append(book_data)

    return {"books": output}


@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {'id': book.id, 'name': book.name, 'author': book.author, 'publisher': book.publisher}


@app.route('/books', methods=['POST'])
def add_book():
    book = Book(id=request.json['id'], name=request.json['name'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}


@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {"error": "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "buh bye!"}