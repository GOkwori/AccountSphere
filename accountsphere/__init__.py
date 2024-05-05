import os 
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager, login_manager

# Import environment variables if available
if os.path.exists("env.py"):    
    import env

app = Flask(__name__)    # Initialize Flask application
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")     # Set the secret key for the application
if os.environ.get("DEVELOPMENT") == "True":    # Check if the application is in development mode
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")   # Set the database URI for the application

else:
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri

# Initialize the application with the database
db = SQLAlchemy(app)    # Initialize SQLAlchemy
migrate = Migrate(app, db)    # Initialize Flask-Migrate
bcrypt = Bcrypt(app)    # Initialize Bcrypt
login_manager = LoginManager(app)    # Initialize 
login_manager.login_view = 'login'    # Set the login view for the application

# Import routes and models from the application
from accountsphere import routes, models    

# User loader function to load the user by ID
@login_manager.user_loader     
def load_user(user_id):
    return models.User.query.get(int(user_id))
