from flask import Blueprint, render_template, request

user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/')
def index():
    return render_template('base.html')


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        pass
    return render_template('user/register.html')
