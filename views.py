from flask import Blueprint, render_template
from auth import login_required

bp = Blueprint('views', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/success', methods=['GET', 'POST'])
@login_required
def success():
    return render_template('success.html')