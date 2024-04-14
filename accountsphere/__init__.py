import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

if os.path.exists("env.py"):
    import env


app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") # Set the secret key
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL") # Set the database URL

db = SQLAlchemy(app)
migrate = Migrate(app, db)  # Initialize the Migrate object with the Flask app and the SQLAlchemy db object
bcrypt = Bcrypt(app)

from accountsphere import routes
