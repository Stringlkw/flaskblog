# from flask import Blueprint, request, render_template, redirect
#
# from apps.user.models import User
# from exts import db
#
# user_bp = Blueprint('user', __name__)
# # 列表保存的是一个一个的用户对象
# users = []
#
#
# @user_bp.route('/')
# def user_center():
#     return render_template('user/show.html', users=users)
#
#
# @user_bp.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         # 获取提交的数据
#         username = request.form.get('username')
#         password = request.form.get('password')
#         repassword = request.form.get('repassword')
#         phone = request.form.get('phone')
#         if password == repassword:
#             user = User()
#             user.username = username
#             user.password = password
#             user.phone = phone
#             db.session.add(user)
#             db.session.commit()
#             return '用户注册成功'
#         else:
#             return '两次密码不一致'
#     return render_template('user/register.html')
#
#
# @user_bp.route('/login', methods=['GET', 'POST'])
# def login():
#     return '用户登录'
#
#
# @user_bp.route('/del')
# def del_user():
#     # 获取传递的username
#     username = request.args.get('username')
#     # 根据username找到列表中的user对象
#     for user in users:
#         if user.username == username:
#             # 删除user
#             users.remove(user)
#             return redirect('/')
#     else:
#         return '删除失败'
#
#
# @user_bp.route('/update', methods=['POST', 'GET'], endpoint='update')
# def update_user():
#     if request.method == 'POST':
#         realname = request.form.get('realname')
#         username = request.form.get('username')
#         password = request.form.get('password')
#         phone = request.form.get('phone')
#         for user in users:
#             if user.username == realname:
#                 user.username = username
#                 user.phone = phone
#                 return '更改成功'
#     else:
#         username = request.args.get('username')
#         for user in users:
#             if user.username == username:
#                 return render_template('user/update.html', user=user)
#
#
# @user_bp.route('/logout', methods=['GET', 'POST'])
# def logout():
#     return '用户退出'