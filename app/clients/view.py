from app.helper import *
from app.model import Client
from flask_uploads import UploadSet, configure_uploads, IMAGES
client_view = Blueprint('client',  __name__, url_prefix='/clients')
photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() +'/app/static/images'
configure_uploads(app, photos)


@client_view.route('/')
def clients():
    all_clients = session.query(Client).all()
    session.close()
    return render_template('public/clients.html', clients=all_clients)


@client_view.route('/new', methods=['GET', 'POST'])
@login_required
def new_client():
    if request.method == 'POST':
        try:
            if 'client_img' in request.files:
                client_img = request.files['client_img']
                img_to_save = photos.save(client_img, folder='clients')
                new = Client(logo=img_to_save, url=photos.url(img_to_save))
                session.add(new)
                session.commit()
                session.close()
                flash("new client successfully added.")
                return redirect(url_for('admin.admin_home'))
            else:
                flash("Please select file to upload")
                return redirect(url_for('admin.admin_home'))
        except Exception:
            abort(500)
    return render_template('admin/NewClient.html')
