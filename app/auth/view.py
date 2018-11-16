from app.helper import *
from app.model import Admin
from controller import *

auth_view = Blueprint('auth', __name__, url_prefix='/staff')


@auth_view.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and not empty_form(request.form):
        if check_password(request.form['email'], request.form['password']):
            login_session['username'] = request.form['email']
            flash('You successfully logged in')
            return redirect(url_for('admin.admin_home'))
    state = csrf_state()
    return render_template('admin/login.html', state=state)


@auth_view.route('/logout')
def logout():
    del login_session['username']
    return redirect(url_for('home.home'))
