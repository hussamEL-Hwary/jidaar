from app.helper import *
from controller import *
from app.model import Career, Contact_info

career_view = Blueprint('career', __name__, url_prefix='/career')


@career_view.route('')
def career():
    careers = session.query(Career).all()
    con = session.query(Contact_info).first()
    session.close()
    return render_template('public/career.html',
                           careers=careers,
                           contact_info=con,
                           active_page='career')


@career_view.route('/new', methods=['GET', 'POST'])
@login_required
def new_career():
    if request.method == 'POST' and validate_form(request.form) is False:
        name = request.form['name']
        description = request.form['description']
        try:
            new_career = Career(name=name, description=description)
            session.add(new_career)
            session.commit()
            session.close()
            flash("new career successfully added")
            return redirect(url_for('admin.admin_home'))
        except exc.SQLAlchemyError:
            abort(500)
    return render_template('admin/AddCareer.html')


@career_view.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_career(id):
    item_to_edit = get_item_by_id(id)
    if not item_to_edit:
        flash("Please select career to edit")
        return redirect(url_for('admin.admin_home'))
    if request.method == 'POST' and validate_form(request.form) is False:
        name = request.form['name']
        description = request.form['description']
        item_to_edit.name = name
        item_to_edit.description = description
        session.add(item_to_edit)
        session.commit()
        session.close()
        flash("career successfully edited")
        return redirect(url_for('admin.admin_home'))
    return render_template('admin/EditExistingCareer.html',
                           career=item_to_edit)


@career_view.route('/edit')
@login_required
def edit_careers():
    careers = session.query(Career).all()
    session.close()
    return render_template('admin/EditCareer.html', careers=careers)


@career_view.route('/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def delete_career(id):
    current_career = get_item_by_id(id)
    if not current_career:
        flash("Please select career to delete")
        return redirect(url_for('admin.admin_home'))
    if request.method == 'POST':
        try:
            session.delete(current_career)
            session.commit()
            session.close()
            flash("career successfully deleted")
        except exc.SQLAlchemyError:
            abort(500)
        return redirect(url_for('admin.admin_home'))
    return render_template('admin/career_delete_confirm.html',
                           career=current_career)
