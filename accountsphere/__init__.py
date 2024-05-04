import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Import environment variables if available
if os.path.exists("env.py"):
    import env

# Initialize Flask application
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "any_secret_key")

# Determine the database URI based on the environment
if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL", "sqlite:///default.db")
else:
    uri = os.environ.get("DATABASE_URL", "sqlite:///default.db")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri

# Initialize database management
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)

# Set up Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Import routes and models at the end to avoid circular dependencies
from accountsphere import models, routes

# User loader function
@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(int(user_id))
