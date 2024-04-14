from flask import render_template, request, redirect, url_for, flash
from flask_bcrypt import Bcrypt
from accountsphere import app, db
from accountsphere.models import User, Group, UserGroup, Customer, Product, Account

bcrypt = Bcrypt(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/user")
def user():
    return render_template("user.html")

@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        password = request.form.get("password")  # Assuming you have a password field
        role = request.form.get("role")

        if not username or not email or not password:
            flash("Username, email, and password are required.", "error")
            return render_template("add_user.html")

        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')

        user = User(username=username, email=email, first_name=first_name, last_name=last_name, password_hash=password_hash, role=role)
        db.session.add(user)
        db.session.commit()
        flash("User added successfully!", "success")
        return redirect(url_for("user"))
    return render_template("add_user.html")

@app.route("/product")
def product():
    return render_template("product.html")

@app.route("/add_product", methods=["GET", "POST"])  # Allow both GET and POST
def add_product():
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        type = request.form.get("type")
        product = Product(name=name, description=description, type=type)
        db.session.add(product)
        db.session.commit()
        return redirect(url_for("product"))
    return render_template("add_product.html")

@app.route("/account")
def account():
    return render_template("account.html")

@app.route("/add_account", methods=["GET", "POST"])  # Allow both GET and POST
def add_account():
    if request.method == "POST":
        customer_id = request.form.get("customer_id")
        product_id = request.form.get("product_id")
        account = Account(customer_id=customer_id, product_id=product_id)
        db.session.add(account)
        db.session.commit()
        return redirect(url_for("account"))
    return render_template("add_account.html")

@app.route("/ad_group")
def ad_group():
    ad_groups = Group.query.order_by(Group.name).all()
    print("Number of groups fetched:", len(ad_groups))  # This will show you how many groups are fetched
    return render_template("ad_group.html", ad_groups=ad_groups)



@app.route("/add_ad_group", methods=["GET", "POST"])  # Allow both GET and POST
def add_ad_group():
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        group_type = request.form.get("group_type")
        group = Group(name=name, description=description, group_type=group_type)
        db.session.add(group)
        db.session.commit()
        return redirect(url_for("ad_group"))
    return render_template("add_ad_group.html")
