from app.helper import session
from app.model import Career


def validate_form(form):
    return form['name'] == '' or form['description'] == ''


def get_item_by_id(id):
    item = session.query(Career).filter_by(id=id).one_or_none()
    session.close()
    return item


def delete_item(item):
    session.delete(item)
    session.commit()