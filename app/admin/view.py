from app.helper import *

admin_view = Blueprint('admin', __name__, url_prefix='/admin')


@admin_view.route('/')
@login_required
def admin_home():
    return render_template('admin/main-page.html')
