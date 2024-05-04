import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from db_config import engine

# Import environment variables if available
if os.path.exists("env.py"):
    import env

# Initialize Flask application
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") # Set the secret key
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL") # Set the database URL

# Initialize database management
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)

# Set up Flask-Login
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Specify the login view name

# Import routes and models at the end to avoid circular dependencies
from accountsphere import models, routes

# User loader function
@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(int(user_id))

with engine.connect() as connection:
    result = connection.execute("SELECT 1")
    print(result.fetchone())
