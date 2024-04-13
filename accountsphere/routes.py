from flask import render_template
from accountsphere import app, db
from accountsphere.models import User, Customer, Product, Account


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/user")
def user():
    return render_template("user.html")


@app.route("/add_user")
def add_user():
    return render_template("add_user.html")


@app.route("/product")
def product():
    return render_template("product.html")


@app.route("/add_product")
def add_product():
    return render_template("add_product.html")


@app.route("/account")
def account():
    return render_template("account.html")


@app.route("/add_account")
def add_account():
    return render_template("add_account.html")


@app.route("/ad_group")
def ad_group():
    return render_template("ad_group.html")


@app.route("/add_ad_group")
def add_ad_group():
    return render_template("add_ad_group.html")

