from flask import Flask, abort, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from forms import LoginForm, SignUpForm, BlogForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://todo_db_0bnc_user:wmn8RupULwcVFdZj0Tinoqx3V6joLqMg@dpg-cqtdkajv2p9s73de0lc0-a.oregon-postgres.render.com/todo_db_0bnc'  # 'sqlite:///users.db'
db = SQLAlchemy(app)

# creating flask login instance
login_manager = LoginManager(app)
# if user is not logged in(i.e @login_required failed) then redirect to 'login' view
login_manager.login_view = 'login'


# data models for database
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    blogs = db.relationship('Blog', backref='user', lazy=True)
    comments = db.relationship('Comment', backref='user', lazy=True)


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(10000))
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments = db.relationship('Comment', backref='blog', lazy=True)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(10000))
    userid = db.Column(db.Integer, db.ForeignKey('user.id'))
    blogid = db.Column(db.Integer, db.ForeignKey('blog.id'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


with app.app_context():
    db.create_all()


# App routing
# register and login views
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = SignUpForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists.')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(
            password, method='pbkdf2:sha256')
        new_user = User(username=username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))

    return render_template('register.html', form=form, title="register")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user)
        flash('Logged in successfully!')
        return redirect(url_for('dashboard'))
    return render_template('login.html', form=form, title="login")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')


# blog views
@app.route('/blog', methods=['GET', 'POST'])
@login_required
def blog_post():
    form = BlogForm()
    if form.validate_on_submit():
        b_post = Blog()
        b_post.title = form.title.data
        b_post.content = form.content.data
        b_post.userid = current_user.id  # Link the blog post to the current user
        db.session.add(b_post)
        db.session.commit()
        flash('New blog posted!', 'success')
        blogs = current_user.blogs
        return redirect(url_for('blog_post'))
    blogs = current_user.blogs
    return render_template('blog.html', blogs=blogs, form=form)


if __name__ == '__main__':
    app.run(debug=True)
