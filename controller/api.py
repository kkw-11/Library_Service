from flask import redirect, request, render_template, jsonify, Blueprint, session, g, flash,url_for
from model.models import BorrowBook, User, Book,BookComment
from mysql_script.db_connect import db
from flask_bcrypt import Bcrypt
import pymysql
import datetime
import re


bp = Blueprint('blueprint',__name__)
bcrypt = Bcrypt()

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('login')
    if user_id is None:
        g.user = None
    else:
        g.user = db.session.query(User).filter(User.email == user_id).first()

@bp.route("/")
def home():
    if session.get('login') is None:
        return redirect("/login")
    else:
        return redirect("/mainBookList")
    
@bp.route("/join",methods=["GET","POST"])
def join():
    if request.method == 'GET':
        return render_template('join.html')
    else:
        email = request.form['email']
        user_pw1 = request.form['pw1']
        user_pw2 = request.form['pw2']
        name = request.form['name']

        if user_pw1 == "" or user_pw2 == "":
            flash("패스워드를 입력하세요")
            return render_template('join.html')

        if name == "":
            flash("이름을 입력하세요")
            return render_template('join.html')

        if user_pw1 != user_pw2:
            flash("패스워드가 일치하지 않습니다.")
            return render_template('join.html')
        
        if len(user_pw1) < 8:
            flash("패스워드를 8자리 이상 입력하세요")
            return render_template('join.html')

        # pw_hash = Bcrypt.generate_password_hash(user_pw)
        user = User(email, user_pw1, name )
        db.session.add(user)
        db.session.commit()
        flash("회원가입 성공!")
        return redirect("/")


@bp.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        email = request.form['email']
        user_pw = request.form['pw']
        user = User.query.filter(User.email == email).first()
        if not user:
            flash("로그인 실패")
            return redirect('/login')
        else:
            if user_pw == user.password:
                session['login'] = user.email
                flash("로그인 성공")
                return redirect('/mainBookList')
            else:
                flash("로그인 실패")
                return redirect('/login')

@bp.route("/logout")
def logout():
    session['login'] = None
    return redirect('/')

@bp.route("/mainBookList")
def mainBookList():
    book_info = Book.query.order_by(Book.book_id).all()
    sum_rating = 0
    for book in book_info:
        sum_rating += book.rating
        
    print(sum_rating)
    return render_template("mainBookList.html", book_list = book_info,avg_rating=sum_rating//len(book_info) )

@bp.route("/borrowBook")
def borrow():
    book_id = request.args.get("data")
    book = Book.query.filter(Book.book_id == book_id).first()
    if book.remaining <=0:
        flash("선택하신 도서는 대여 불가입니다.")
        return render_template('mainBookList.html')
    book.remaining = book.remaining -1
    db.session.add(book)

    email = session.get('login')
    now = datetime.datetime.now().date()

    borrow = BorrowBook(book_id, email, now)
    db.session.add(borrow)
    db.session.commit()
    flash("대여 성공!")
    return redirect("/mainBookList")

@bp.route("/returnBookList")
def returnBookList():
    login_email = session.get('login')
    if login_email is None:
            return redirect("/login")
    else:
        borrow_book_list = BorrowBook.query.filter((BorrowBook.email == login_email) & BorrowBook.return_date ==None).all()
        return render_template("returnBook.html", book_list = borrow_book_list)

@bp.route("/returnBook")
def returnBook():
    login_email = session.get('login')
    if login_email is None:
        return redirect("/login")
    else:
        return_book = request.args.get("data")
        borrow_return_book = request.args.get("data2")
        book = Book.query.filter(Book.book_id == return_book).first()
        book.remaining = book.remaining + 1

        borrowbook = BorrowBook.query.filter(BorrowBook.id == borrow_return_book).first()
        borrowbook.return_date = datetime.datetime.now().date()
        db.session.add(book)
        db.session.add(borrowbook)
        db.session.commit()
        data = BorrowBook.query.filter((BorrowBook.email == login_email) & BorrowBook.return_date ==None).all()

        flash("반납 성공!")
        return redirect("/returnBookList")
        return render_template("returnBook.html", book_list = data)
        
        # data = BorrowBook.query.filter(BorrowBook.email == login_email).all()
        # return render_template("returnBook.html", book_list = data)


@bp.route("/bookIDetail")
def bookIDetail():
    book_id = request.args.get("name")
    print(type(book_id))
    data = Book.query.filter(Book.book_id == book_id).first()
    bookcomment = BookComment.query.filter(BookComment.book_id == int(book_id)).all()

    return render_template("bookIDetail.html",book = data,bookcomment=bookcomment)

@bp.route("/post", methods=["GET","POST"])
def post():
    content = request.form['content']
    book_id = request.args.get("book")
    email = session.get('login')
    book_data = Book.query.filter(Book.book_id == book_id).first()

    bookcomment = BookComment.query.filter(BookComment.book_id == int(book_id)).all()
    print(bookcomment)
    print(content,type(book_id),email)


    if email is None or book_id is None:
        return redirect('/login')
    else:
        content = BookComment(int(book_id), email, content)
        db.session.add(content)
        db.session.commit()
        return render_template("bookIDetail.html",book = book_data, bookcomment=bookcomment)

@bp.route("/borrowBookList")
def borrowBookList():
    if session.get('login') is None:
        return redirect("/login")
    else:
        email = session.get('login')
        rental_list = BorrowBook.query.filter(BorrowBook.email == email).all()
        return render_template("borrowBookList.html",rental_list = rental_list)

