# import flask
from flask import (Flask,
                   render_template,
                   redirect,
                   request,
                   url_for,
                   Blueprint,
                   abort,
                   flash,
                   session as login_session)

from functools import wraps
# import sqlalchemy
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from model import base
import os


app = Flask(__name__)
app.secret_key = 'secret_key'


# connect to db
def init_db():
    engine = create_engine('sqlite:///app/database.db',
                           connect_args={'check_same_thread': False})
    base.metadata.bind = engine
    DBsession = sessionmaker(bind=engine)
    return DBsession()


# create database session
session = init_db()


# login required decorator function
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in login_session:
            flash('You have to login')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function


# delete file from server
def delete_file(path):
    try:
        os.remove(path)
        return True
    except:
        return False
# handel 404 error
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# handel 500 error
@app.errorhandler(500)
def permission_denied(e):
    return render_template('500.html'), 401
