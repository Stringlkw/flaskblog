from flask import Blueprint, render_template, request

from apps.user.models import User

article_bp = Blueprint('article', __name__)


@article_bp.route('/publish', methods=['GET', 'POST'])
def publish_article():
    if request.method == 'POST':
        pass
    else:
        users = User.query.filter(User.isdelete == False).all()
        return render_template('‘article/add_article.html)', users=users)
