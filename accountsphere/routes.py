from flask import render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from accountsphere import app, db
from accountsphere.models import User, Group, Product, Account, NewsItem
from sqlalchemy.orm import joinedload
from datetime import datetime
from flask_login import login_user, logout_user, current_user, login_required


@app.route("/")
def home():
    news_items = NewsItem.query.all()
    return render_template('index.html', news_items=news_items)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        if not all([first_name, last_name, username, email, password]):
            flash("All fields are required.", "error")
            return render_template("register.html")

        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            flash("Username or email already exists.", "error")
            return render_template("register.html")

        hashed_password = generate_password_hash(password, method='sha256')
        user = User(first_name=first_name, last_name=last_name, username=username, email=email, password_hash=hashed_password, role='User')
        db.session.add(user)
        db.session.commit()
        flash("User registered successfully!", "success")
        return redirect(url_for("login"))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash("Login successful!", "success")
            return redirect(url_for("home"))
        else:
            flash("Invalid username or password.", "error")
            return render_template("login.html")

    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("home"))


@app.route("/user")
def user():
    users = User.query.order_by(User.first_name, User.last_name).all()
    return render_template("user.html", users=users)


@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    groups = Group.query.all()
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        role = request.form.get("role")

        if not all([username, email, first_name, last_name]):
            flash("All fields are required.", "error")
            return render_template("add_user.html", groups=groups)

        user = User(username=username, email=email, first_name=first_name, last_name=last_name, role=role)
        db.session.add(user)
        db.session.commit()
        flash("User added successfully!", "success")
        return redirect(url_for("user"))
    return render_template("add_user.html", groups=groups)


@app.route("/edit_user/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
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
    return render_template("edit_user.html", user=user)


@app.route("/delete_user/<int:user_id>")
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    flash("User deleted successfully!", "success")
    return redirect(url_for("user"))


@app.route("/user_search")
def user_search():
    query = request.args.get('query', '')
    users = User.query.filter(
        (User.first_name.ilike(f'%{query}%')) |
        (User.last_name.ilike(f'%{query}%')) |
        (User.username.ilike(f'%{query}%')) |
        (User.email.ilike(f'%{query}%'))
    ).all()
    return render_template('user.html', users=users)


@app.route("/product")
def product():
    products = list(Product.query.order_by(Product.name).all())
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


@app.route("/product_search")
def product_search():
    query = request.args.get('query', '')
    products = Product.query.filter(
        (Product.name.ilike(f'%{query}%')) |
        (Product.description.ilike(f'%{query}%')) |
        (Product.type.ilike(f'%{query}%'))
    ).all()
    return render_template('product.html', products=products)


@app.route("/account")
def account():
    # Fetch accounts and their related product names using joined load,
    # sorted by first name and then last name
    accounts = Account.query \
        .options(db.joinedload(Account.product)) \
        .order_by(Account.first_name, Account.last_name).all()

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


@app.route('/account_search')
def account_search():
    query = request.args.get('query', '')
    accounts = Account.query.options(joinedload(Account.product)).filter(
        (Account.first_name.ilike(f'%{query}%')) |
        (Account.last_name.ilike(f'%{query}%')) |
        (Account.email.ilike(f'%{query}%')) |
        (Account.phone_number.ilike(f'%{query}%'))
    ).all()
    # Add product names to the account objects for easier access in the template
    for account in accounts:
        account.product_name = account.product.name if account.product else 'No Product'
    return render_template('account.html', accounts=accounts)


@app.route("/ad_group")
def ad_group():
    ad_groups = list(Group.query.order_by(Group.name).all())
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


@app.route("/ad_group_search")
def ad_group_search():
    query = request.args.get('query', '')
    ad_groups = Group.query.filter(
        (Group.name.ilike(f'%{query}%')) |
        (Group.description.ilike(f'%{query}%')) |
        (Group.group_type.ilike(f'%{query}%'))
    ).all()
    return render_template('ad_group.html', ad_groups=ad_groups)


@app.route("/news")
def news():
    news_items = NewsItem.query.all()
    return render_template("news.html", news_items=news_items)


@app.route('/add_news', methods=["GET", "POST"])
def add_news():
    if request.method == "POST":
        headline = request.form.get("headline")
        description = request.form.get("description")
        news_item = NewsItem(headline=headline, description=description)
        db.session.add(news_item)
        db.session.commit()
        return redirect(url_for("news"))
    return render_template("add_news.html")


@app.route('/edit_news/<int:news_id>', methods=["GET", "POST"])
def edit_news(news_id):
    news_item = NewsItem.query.get_or_404(news_id)
    if request.method == "POST":
        news_item.headline = request.form.get("headline")
        news_item.description = request.form.get("description")
        db.session.commit()
        return redirect(url_for("news"))

    news_items = NewsItem.query.all()  # This will fetch all news items for listing
    return render_template("edit_news.html", news_item=news_item, news_items=news_items)


@app.route('/delete_news/<int:news_id>')
def delete_news(news_id):
    news_item = NewsItem.query.get_or_404(news_id)
    db.session.delete(news_item)
    db.session.commit()
    return redirect(url_for("news"))


@app.route('/news_search')
def news_search():
    query = request.args.get('query', '')
    news_items = NewsItem.query.filter(
        (NewsItem.headline.ilike(f'%{query}%')) |
        (NewsItem.description.ilike(f'%{query}%'))
    ).all()
    return render_template('news.html', news_items=news_items)
