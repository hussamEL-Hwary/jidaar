from app.helper import *
from app.model import Admin
admin_view = Blueprint('admin', __name__, url_prefix='/admin')


@admin_view.route('/')
@login_required
def admin_home():
    return render_template('admin/main-page.html')


@admin_view.route('/edit')
@login_required
def update_info():
    current_admin = session.query(Admin).first()
    return render_template('admin/edit_info.html',
                           admin_email=current_admin.user_name)


@admin_view.route('/edit/email', methods=['POST'])
@login_required
def update_email():
    try:
        email = request.form['email']
        if len(email) > 20:
            flash("Email must be less than 21 character")
            return redirect(url_for('admin.update_info'))
        current_admin = session.query(Admin).first()
        current_admin.user_name = email
        session.commit()
        flash("Email successfully updated")
        return redirect(url_for('admin.admin_home'))
    except Exception:
        abort(500)


@admin_view.route('/edit/pass', methods=['POST'])
@login_required
def edit_password():
    password = request.form['new_pass']
    confirm_password = request.form['re_new_pass']
    if password != confirm_password:
        flash("password must match")
        return redirect(url_for('admin.update_info'))
    current_admin = session.query(Admin).first()
    current_admin.hash_password(password)
    session.commit()
    flash("password successfully updated")
    return redirect(url_for('admin.admin_home'))