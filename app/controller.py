from flask import (
    Blueprint, render_template
)

from app.db import get_db

#db, c = get_db()
#c.execute('SELECT * FROM user')
#user = c.fetchone()

bp = Blueprint("controller", __name__, url_prefix='/')

@bp.route("/", methods=['GET', 'POST'])
def index():
    return render_template('login/login.html')