from app.helper import *
from flask_uploads import UploadSet, configure_uploads, IMAGES
from app.model import Project, Project_images, Contact_info
from shutil import rmtree
import math
from controller import *
project_view = Blueprint('project', __name__, url_prefix='/project')


photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() +'/app/static/images'
configure_uploads(app, photos)


# make 3 arrays of the projects
@project_view.route('')
def all_projects():
    projects = session.query(Project).all()
    con = session.query(Contact_info).first()
    parts = int(math.floor(len(projects)/3.0))
    first_p, second_p, third_p = projects[:parts], projects[parts:parts*2], projects[parts*2:]
    return render_template('public/projects.html',
                           col1=first_p,
                           col2=second_p,
                           col3=third_p,
                           contact_info = con)


@project_view.route('<int:id>/view')
def single_project(id):
    project = session.query(Project).filter_by(id=id).one_or_none()
    con = session.query(Contact_info).first()
    if not project:
        flash("Please select project")
        return redirect(url_for('project.all_projects'))
    return render_template('public/single_project.html',
                           project=project,
                           contact_info=con)


@project_view.route('/edit')
@login_required
def edit():
    projects = session.query(Project).all()
    session.close()
    return render_template('admin/EditProjects.html', projects=projects)


@project_view.route('/new', methods=['GET', 'POST'])
@login_required
def new_project():
    if request.method == 'POST':
        project_images = request.files.getlist("files[]")
        name = request.form['project_name']
        role = request.form['role']
        location = request.form['location']
        status = request.form['status']
        area = request.form['area']
        try:
            project = Project(name=name,
                              role=role,
                              location=location,
                              status=status,
                              area=area)
            session.add(project)
            session.commit()

            for img in project_images:
                current_img = photos.save(img, folder="projects/"+str(project.id))
                db_img = Project_images(project_id=project.id, img_url=photos.url(current_img))
                session.add(db_img)
                session.commit()
            flash("New project successfully added")
        except exc.SQLAlchemyError:
            abort(500)
        finally:
            session.close()
        return redirect(url_for('admin.admin_home'))
    return render_template('admin/AddProject.html')


@project_view.route('/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def delete_project(id):
    project_to_delete = session.query(Project).filter_by(id=id).one_or_none()
    session.close()
    if not project_to_delete:
        flash("Please select project to delete")
        return redirect(url_for('admin.admin_home'))
    if request.method == 'POST':
        try:
            session.delete(project_to_delete)
            session.commit()
            session.close()
            flash("Project successfully deleted")
            rmtree(os.getcwd()+'/app/static/images/projects/'+str(project_to_delete.id))
        except Exception:
            abort(500)
        finally:
            session.close()
        return redirect(url_for('admin.admin_home'))
    return render_template('admin/project_delete_confirm.html',
                           project=project_to_delete)


@project_view.route('/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_project(id):
    project_to_edit = session.query(Project).filter_by(id=id).one_or_none()
    session.close()
    if not project_to_edit:
        flash("Please select project to delete")
        return redirect(url_for('admin.admin_home'))
    if request.method == 'POST' and validate_form(request.form):
        try:
            project_images = request.files.getlist("files[]")
            project_to_edit.name = request.form['project_name']
            project_to_edit.role = request.form['role']
            project_to_edit.location = request.form['location']
            project_to_edit.area = request.form['area']
            project_to_edit.status = request.form['status']
            session.add(project_to_edit)
            session.commit()
            for img in project_images:
                current_img = photos.save(img, folder="projects/" + str(project_to_edit.id))
                db_img = Project_images(project_id=project_to_edit.id, img_url=photos.url(current_img))
                session.add(db_img)
                session.commit()
            flash("New project successfully updated")
        except Exception:
            abort(500)
        finally:
            session.close()
        return redirect(url_for('admin.admin_home'))
    return render_template('admin/EditExistingProject.html',
                           project=project_to_edit)
