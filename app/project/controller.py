
def validate_form(form):
    if form['project_name'] == '' \
            or form['role'] == '' or form['location'] == '' \
            or form['status'] == '' or form['area'] == '':
        return False
    return True
