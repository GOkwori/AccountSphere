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
    users = User.query.all()
    print("Number of users fetched:", len(users))  # This will show you how many users are fetched
    for user in users:
        print(user.username, user.email)  # This will print each user's username and email to the console
    return render_template("user.html", users=users)


@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    groups = Group.query.all()  # Fetch all groups from the database
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        role = request.form.get("role")

        if not username or not email:
            flash("Username, and email are required.", "error")
            return render_template("add_user.html", groups=groups)

        user = User(username=username, email=email, first_name=first_name, last_name=last_name, role=role)
        db.session.add(user)
        db.session.commit()
        flash("User added successfully!", "success")
        return redirect(url_for("user"))
    else:
        return render_template("add_user.html", groups=groups)


@app.route("/product")
def product():
    products = Product.query.order_by(Product.name).all()
    print("Number of products fetched:", len(products))
    return render_template("product.html", products=products)

@app.route("/add_product", methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        product_type = request.form.get("type")

        if not name or not product_type:  # Validate required fields
            flash("Product name and type are required.", "error")
            return render_template("add_product.html")

        product = Product(name=name, description=description, type=product_type)
        db.session.add(product)
        try:
            db.session.commit()
            flash("Product added successfully!", "success")
            return redirect(url_for("product"))
        except Exception as e:
            db.session.rollback()
            flash("Error adding product: " + str(e), "error")
            return render_template("add_product.html")
    return render_template("add_product.html")

@app.route("/account")
def account():
    accounts = Account.query.all()
    print("Number of accounts fetched:", len(accounts))
  
    return render_template("account.html", accounts=accounts)



@app.route("/add_account", methods=["GET", "POST"])  # Allow both GET and POST
def add_account():
    products = Product.query.all()  # Fetch all products from the database

    if request.method == "POST":
        customer_id = request.form.get("customer_id")
        product_id = request.form.get("product_id")  # This will now come from the dropdown
        account = Account(customer_id=customer_id, product_id=product_id)
        db.session.add(account)
        try:
            db.session.commit()
            flash("Account created successfully!", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"An error occurred: {str(e)}", "error")

        return redirect(url_for("account"))

    return render_template("add_account.html", products=products)  # Pass products to the template for the dropdown


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
