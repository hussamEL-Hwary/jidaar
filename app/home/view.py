# -*- coding: utf-8 -*-
from app.helper import *
from app.model import (Basic,
                       Contact_info,
                       Client,
                       About,
                       Letters,
                       Project,
                       Project_images)
from flask_uploads import UploadSet, configure_uploads, IMAGES, DOCUMENTS
from werkzeug.utils import secure_filename
home_view = Blueprint('home', __name__, url_prefix='/')
photos = UploadSet('photos', IMAGES+tuple('pdf'))
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() +'app/static/images'
configure_uploads(app, photos)


@home_view.route('/')
def home():
    bascic_info = session.query(Basic).first()
    clients = session.query(Client).all()
    con = session.query(Contact_info).first()
    main_projects = session.query(Project).order_by(Project.id).limit(4)
    session.close()
    return render_template('public/home.html',
                           info=bascic_info,
                           clients=clients,
                           contact_info=con,
                           projects=main_projects,
                           active_page='home')

@home_view.route('/basic/edit', methods=['GET', 'POST'])
@login_required
def edit_basic_info():
    basic_info = session.query(Basic).first()
    session.close()
    if request.method == 'POST':
        new_mission = request.form['new_mission']
        new_vision = request.form['new_vision']
        new_values = request.form['new_values']
        basic_info.mission = new_mission
        basic_info.vision = new_vision
        basic_info.values = new_values
        if 'certification_img' in request.files:
            try:
                filename = photos.save(request.files['certification_img'], name="certification.")
                delete_file(photos.path(basic_info.certification_name))
                basic_info.certification_name = filename
                basic_info.certification_url = photos.url(filename)
            except Exception:
                abort(500)

        session.add(basic_info)
        session.commit()
        session.close()
        return redirect(url_for('admin.admin_home'))
    return render_template('admin/EditHome.html', info=basic_info)


@home_view.route('/contact')
def contact():
    con = session.query(Contact_info).first()
    session.close()
    return render_template('public/contact.html', contact_info=con,
                           active_page='contact')


@home_view.route('/contact/edit', methods=['GET', 'POST'])
@login_required
def edit_contact():
    contact_info = session.query(Contact_info).first()
    if request.method == 'POST':
        contact_info.address = request.form['address']
        contact_info.email = request.form['email']
        contact_info.phone = request.form['phone']
        contact_info.fax = request.form['fax']
        contact_info.mobile = request.form['mobile']
        session.add(contact_info)
        session.commit()
        flash("Contact info successfully updated")
        return redirect(url_for('admin.admin_home'))
    return render_template('admin/EditContact.html', contact=contact_info)


@home_view.route('/services')
def services():
    con = session.query(Contact_info).first()
    session.close()
    return render_template('public/services.html', contact_info=con,
                           active_page='services')


@home_view.route('/about')
def about():
    con = session.query(Contact_info).first()
    letters = session.query(Letters).all()
    about_data = session.query(About).first()
    session.close()
    return render_template('public/about.html',
                           contact_info=con,
                           letters=letters,
                           about_data=about_data,
                           active_page='about')


@home_view.route('/about/edit', methods=['GET', 'POST'])
@login_required
def edit_about():
    about = session.query(About).first()
    if request.method == 'POST':
        try:
            about.history = request.form['history']
            about.iso_description = request.form['iso']
            about.ohsas_description = request.form['ohsas']

            if 'letter' in request.files:
                # upload new letter to server
                new_letter = request.files['letter']
                saved_letter = photos.save(new_letter, folder='letters')
                print saved_letter
                # save letter utl to db
                db_letter = Letters(name=photos.path(saved_letter),
                                    url=photos.url(saved_letter))
                session.add(db_letter)
                session.commit()
            if 'iso_img' in request.files:
                # delete old iso img
                delete_file(about.iso_name)
                # save the new to server
                new_iso_img = request.files['iso_img']
                saved_iso_img = photos.save(new_iso_img)
                # save url to db
                about.iso_name = photos.path(saved_iso_img)
                about.iso_url = photos.url(saved_iso_img)
            if 'ohsas_img' in request.files:
                # delete old ohsas img
                delete_file(about.ohsas_name)
                # save the new to server
                new_ohsas_img = request.files['ohsas_img']
                saved_ohsas_img = photos.save(new_ohsas_img)
                # save url to db
                about.ohsas_name = photos.path(saved_ohsas_img)
                about.ohsas_url = photos.url(saved_ohsas_img)
            if 'code_of_conduct' in request.files:
                # delete old code of conduct
                delete_file(about.code_of_conduct_name)
                # save the new to server
                new_code = request.files['code_of_conduct']
                code_name = secure_filename(new_code.filename)
                new_code.save(app.config['UPLOADED_PHOTOS_DEST']+"/"+code_name)
                # save url to db
                about.code_of_conduct_name = photos.path(new_code.filename)
                about.code_of_conduct_url = photos.url(new_code.filename)
            if 'brochure' in request.files:
                # delete old code of conduct
                delete_file(about.brochure_name)
                # save the new to server
                new_brochure = request.files['brochure']
                brochure_name = secure_filename(new_brochure.filename)
                new_brochure.save(app.config['UPLOADED_PHOTOS_DEST']+"/"+brochure_name)
                # save url to db
                about.brochure_name = photos.path(new_brochure.filename)
                about.brochure_url = photos.url(new_brochure.filename)
            session.add(about)
            session.commit()
            session.close()
            return redirect(url_for('admin.admin_home'))
        except Exception:
            abort(500)
    return render_template('admin/EditAbout.html', about=about)
