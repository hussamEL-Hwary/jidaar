import string, random
from app.helper import *
from app.model import Admin


# Create 'state' token to protect against anti-forgery attacks
def csrf_state():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for i in range(32))


# check if login form is empty or not
def empty_form(form):
    return len(form['email']) == 0 or len(form['password']) == 0


def check_password(username, password):
    try:
        admin = session.query(Admin).filter_by(user_name=username).one_or_none()
        if not admin:
            return False
        if admin.verify_password(password):
            return True
    except exc.SQLAlchemyError:
        return False
