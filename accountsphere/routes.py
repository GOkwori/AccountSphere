from flask import render_template, request, redirect, url_for, flash
from accountsphere import app, db
from accountsphere.models import User, Group, UserGroup, Product, Account
from datetime import datetime

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


@app.route("/edit_user/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    groups = Group.query.all() 
    user = User.query.get_or_404(user_id)
    if request.method == "POST":
        user.username = request.form.get("username")
        user.email = request.form.get("email")
        user.first_name = request.form.get("first_name")
        user.last_name = request.form.get("last_name")
        user.role = request.form.get("role")
        db.session.commit()
        flash("User updated successfully!", "success")
        return redirect(url_for("user"))
    return render_template("edit_user.html", groups=groups, user=user)


@app.route("/delete_user/<int:user_id>")
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash("User deleted successfully!", "success")
    return redirect(url_for("user"))


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


@app.route("/edit_product/<int:product_id>", methods=["GET", "POST"])
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    if request.method == "POST":
        product.name = request.form.get("name")
        product.description = request.form.get("description")
        product.type = request.form.get("type")
        db.session.commit()
        flash("Product updated successfully!", "success")
        return redirect(url_for("product"))
    return render_template("edit_product.html", product=product)


@app.route("/delete_product/<int:product_id>")
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash("Product deleted successfully!", "success")
    return redirect(url_for("product"))


@app.route("/account")
def account():
    print("Fetching accounts...")
    accounts = Account.query.all()
    # Format balance for each account
    for account in accounts:
        account.balance = "{:,.2f}".format(account.balance)
    return render_template("account.html", accounts=accounts)



@app.route('/add_account', methods=['GET', 'POST'])
def add_account():
    products = Product.query.all()  # Fetch all products for the form dropdown
    if request.method == 'POST':
        # Extract data from form
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        date_of_birth = request.form.get('date_of_birth')
        product_id = request.form.get('product_id')
        account_type = request.form.get('account_type')
        balance = request.form.get('balance') or 0.00
        currency = request.form.get('currency')
        
        # Create new Account instance
        account = Account(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            date_of_birth=date_of_birth,
            product_id=product_id,
            account_type=account_type,
            balance=balance,
            currency=currency,
            status='active'  # Assuming new accounts are always active
        )
        
        # Add to the database
        db.session.add(account)
        try:
            db.session.commit()
            flash('Account created successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error creating account: {e}', 'error')
        
        return redirect(url_for('account'))

    return render_template('add_account.html', products=products)


@app.route('/edit_account/<int:account_id>', methods=['GET', 'POST'])
def edit_account(account_id):
    account = Account.query.get_or_404(account_id)
    products = Product.query.all()
    if request.method == 'POST':
        # Extract data from form
        account.first_name = request.form.get('first_name')
        account.last_name = request.form.get('last_name')
        account.email = request.form.get('email')
        account.phone_number = request.form.get('phone_number')
        account.date_of_birth = request.form.get('date_of_birth')
        account.product_id = request.form.get('product_id')
        account.account_type = request.form.get('account_type')
        account.balance = request.form.get('balance') or 0.00
        account.currency = request.form.get('currency')
        
        # Update the account
        db.session.commit()
        flash('Account updated successfully!', 'success')
        return redirect(url_for('account'))
    
    return render_template('edit_account.html', account=account, products=products)


@app.route('/delete_account/<int:account_id>')
def delete_account(account_id):
    account = Account.query.get_or_404(account_id)
    db.session.delete(account)
    db.session.commit()
    flash('Account deleted successfully!', 'success')
    return redirect(url_for('account'))


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


@app.route("/edit_ad_group/<int:group_id>", methods=["GET", "POST"])
def edit_ad_group(group_id):
    group = Group.query.get_or_404(group_id)
    if request.method == "POST":
        group.name = request.form.get("name")
        group.description = request.form.get("description")
        group.group_type = request.form.get("group_type")
        db.session.commit()
        flash("Group updated successfully!", "success")
        return redirect(url_for("ad_group"))
    return render_template("edit_ad_group.html", group=group)


@app.route("/delete_ad_group/<int:group_id>")
def delete_ad_group(group_id):
    group = Group.query.get_or_404(group_id)
    db.session.delete(group)
    db.session.commit()
    flash("Group deleted successfully!", "success")
    return redirect(url_for("ad_group"))
