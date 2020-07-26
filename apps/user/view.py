from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from apps.user.models import User
from exts import db

user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/')
def index():
    uid = request.cookies.get('uid', None)
    if uid:
        user = User.query.get(uid)
        return render_template('user/index.html', user=user)
    else:
        return render_template('user/index.html')


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        repassword = request.form.get('repassword')
        phone = request.form.get('phone')
        email = request.form.get('email')
        if password == repassword:
            # 注册用户
            user = User()
            user.username = username
            # 密码加密
            user.password = generate_password_hash(password)
            user.phone = phone
            user.email = email
            # 添加并提交
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user.index'))
        else:
            return render_template('user/register.html')
    return render_template('user/register.html')


@user_bp.route('/checkphone', methods=['GET', 'POST'])
def check_phone():
    phone = request.args.get('phone')
    user = User.query.filter(User.phone == phone).all()
    if user:
        return jsonify(code=400, msg='此号码已注册')
    else:
        return jsonify(code=200, msg='此号码可用')


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        users = User.query.filter(User.username == username).all()
        for user in users:
            # 如果flag为True表示密码匹配，否则不匹配
            flag = check_password_hash(user.password, password)
            if flag:
                response = redirect(url_for('user.index'))
                response.set_cookie('uid', str(user.id), max_age=1800)
                return response
        else:
            return render_template('user/login.html', msg='用户名或密码错误')
    else:
        return render_template('user/login.html')


@user_bp.route('logout')
def logout():
    response = redirect(url_for('user.index'))
    # 通过response对象的delete_cookie(key)， key为要删除的cookie的key
    response.delete_cookie('uid')
    return response
