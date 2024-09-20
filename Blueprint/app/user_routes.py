from flask import Blueprint, render_template

user_bp = Blueprint('user', __name__, template_folder='templates/users' )

@user_bp.route('/user')
def user():
    return render_template('login.html')

@user_bp.route('/user2')
def user2():
    return render_template('perfil.html')