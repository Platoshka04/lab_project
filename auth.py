from app import db
from flask import request, render_template, Blueprint, flash, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from models import User


bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route("/register", methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if username and password:
            existing_user = db.session.execute(db.select(User).where(User.username == username)).first()
            if existing_user:
                error = f"Username {username} already exist"
            else: 
                user = User(
                    username = username,
                    password = generate_password_hash(password)
                )
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')
 

@bp.route("/login", methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        user = db.session.execute(db.select(User).where(User.username == username)).scalar_one_or_none()

        if user:
            if check_password_hash(user.password, password):
                session['username'] = username
                return redirect(url_for('views.success'))
            else:
                error = "Check your credentials"
        else:
            error = "User does not exist"

        flash(error)

    return render_template('auth/login.html')


@bp.route('/logout', methods=['GET', 'POST'])
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


def login_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not "username" in session.keys():
            return redirect(url_for('index'))
        return func(*args, **kwargs)

    return decorated_view