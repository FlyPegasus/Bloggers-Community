# Flask Blogging App

This is a simple blogging web application built with Flask, SQLAlchemy, and Flask-Login. Users can register, log in, write blog posts, and comment on them.

## Features

- User Authentication (Registration, Login, Logout)
- Post Blogs (Title & Content)
- Comments on Blog Posts
- Dashboard for managing blogs
- Database integration with SQLAlchemy

## Technologies Used

- **Backend Framework**: Flask
- **Database**: PostgreSQL (SQLAlchemy as ORM)
- **Authentication**: Flask-Login
- **Password Security**: Werkzeug (for password hashing)
- **Frontend**: HTML & Flask templates (using Jinja2)

## Setup Instructions

### Prerequisites

- Python 3.x
- PostgreSQL database (or SQLite if using a different database URI)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/flask-blog-app.git
   cd flask-blog-app
   ```
2. **Create a virtual environment**:
   ```python
   python3 -m venv blogapp
   source blogapp/bin/activate
   # On Windows use:
   blogapp\Scripts\activate
   ```
3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure the Database**:

- In the `app.config['SQLALCHEMY_DATABASE_URI']` section of the code, set up your PostgreSQL connection or replace it with the appropriate database URI. Example for SQLite:

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your-database.db'
```

5. **Initialize the database**: Start a Python shell and run the following commands to create the tables:

```bash
python
from app import db
db.create_all()
exit()
```

6. **Run the application**:

```bash
python app.py
```

The app will be available at http://127.0.0.1:5000

### Forms

The app requires custom form classes that are used in the registration, login, and blog posting views. These forms are defined in the `forms.py` file:

- **LoginForm**: Handles login input for username and password.
- **SignUpForm**: Handles registration input for new users.
- **BlogForm**: Handles creating new blog posts with title and content.

### Routes

- `/register`: User registration.
- `/login`: User login.
- `/logout`: Log out the current user.
- `/dashboard`: User dashboard displaying their blog posts.
- `/blog`: Create and view blog posts.

### Database Models

- **User**: Stores user information and authentication details.
- **Blog**: Stores blog posts linked to a user.
- **Comment**: Stores comments on blog posts, linked to both user and blog.

### Security

- Passwords are hashed using `pbkdf2:sha256` for secure storage.
- Login is required for posting blogs and comments.
