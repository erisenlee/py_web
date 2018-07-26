from sqlalchemy import func
from py_web.models import Post, Tag, Comment, tags
from py_web.database import db
from flask import (redirect, render_template, flash, url_for, Blueprint)
from py_web.forms import CommentForm
from datetime import datetime

def siderbar_data():
    recent = Post.query.order_by(Post.pub_date.desc()).limit(5).all()

    top_tags = db.session.query(Tag, func.count(tags.c.post_id).label('total')).join(
        tags
    ).group_by(Tag).order_by('total DESC').limit(5).all()
    return recent, top_tags


blog = Blueprint('blog',__name__, url_prefix='/blog')


@blog.route('/')
@blog.route('/<int:page>')
def blog_home(page=1):
    posts = Post.query.order_by(Post.pub_date.desc()).paginate(page, 10)
    recent, top_tags = siderbar_data()

    return render_template('blog/blog_home.html',
                           posts=posts,
                           recent=recent,
                           top_tags=top_tags)



@blog.route('/post/<int:post_id>',methods=['GET','POST'])
def post(post_id):
    form=CommentForm()
    if form.validate_on_submit():
        new_comment=Comment(text=form.text.data,date=datetime.now(),post_id=post_id)
        db.session.add(new_comment)
        db.session.commit()
    post=Post.query.get_or_404(post_id)
    tags=post.tags
    comments=post.comments.order_by(Comment.date.desc()).all()
    recent,top_tags=siderbar_data()


    return render_template('blog/post.html',
                           post=post,
                           tags=tags,
                           comments=comments,
                           recent=recent,
                           top_tags=top_tags,
                           form=form
                           )