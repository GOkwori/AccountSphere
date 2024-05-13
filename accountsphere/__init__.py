import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, login_manager

# Import environment variables if available
if os.path.exists("env.py"):
    import env

# Initialize Flask application
app = Flask(__name__)

# Set the secret key for the application
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

# Check if the application is in development mode
if os.environ.get("DEVELOPMENT") == "True":

    # Set the database URI for the application
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri

# Initialize the application with the database
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'
login_manager.anonymous_user = AnonymousUser

# Import routes and models from the application
from accountsphere import routes, models
from .models import AnonymousUser

# User loader function to load the user by ID
@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(int(user_id))
