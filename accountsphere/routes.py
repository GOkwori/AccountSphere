from flask import render_template
from accountsphere import app, db
from accountsphere.models import User, Customer, Product, Account


@app.route("/")
def home():
    return render_template("index.html") 