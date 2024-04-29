from flask import render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from accountsphere import app, db
from accountsphere.models import User, Group, Product, Account, NewsItem
from sqlalchemy.orm import joinedload
from datetime import datetime
from flask_login import login_user, logout_user, login_required


@app.route("/")
def home():
    news_items = NewsItem.query.all()
    return render_template('index.html', news_items=news_items)


@app.route("/register", methods=["GET", "POST"])
def register():
    groups = Group.query.all()

    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")

        if User.query.filter_by(username=username).first():
            flash("Username already exists.", "error")
            return render_template("register.html", groups=groups)
        if User.query.filter_by(email=email).first():
            flash("Email already exists.", "error")
            return render_template("register.html", groups=groups)

        new_user = User(
            first_name=request.form.get("first_name"),
            last_name=request.form.get("last_name"),
            username=username,
            email=email,
            password_hash=generate_password_hash(request.form.get("password")),
            role=request.form.get("role")
        )
        db.session.add(new_user)
        db.session.commit()
        
        flash("Account created successfully! You will be redirected to login.", "success")
        return render_template("register.html", groups=groups, success=True)

    return render_template("register.html", groups=groups)


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

        if User.query.filter_by(username=username).first():
            flash("Username already exists.", "error")
            return render_template("add_user.html", groups=groups)
        if User.query.filter_by(email=email).first():
            flash("Email already exists.", "error")
            return render_template("add_user.html", groups=groups)

        new_user = User(
            first_name=request.form.get("first_name"),
            last_name=request.form.get("last_name"),
            username=username,
            email=email,
            password_hash=generate_password_hash(request.form.get("password")),
            role=request.form.get("role")
        )
        db.session.add(new_user)
        db.session.commit()
        
        flash("User created successfully! You will be redirected to the Users Dashboard.", "success")
        return render_template("add_user.html", groups=groups, success=True)

    return render_template("add_user.html", groups=groups)


@app.route("/edit_user/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    groups = Group.query.all()
    
    if request.method == "POST":
        user.first_name = request.form.get("first_name")
        user.last_name = request.form.get("last_name")
        user.username = request.form.get("username")
        user.email = request.form.get("email")
        user.role = request.form.get("role")

        db.session.add(user)
        db.session.commit()
        flash("User updated successfully!", "success")
        return render_template("edit_user.html", user=user, groups=groups, success=True)
    
    return render_template("edit_user.html", user=user, groups=groups)


@app.route("/delete_user/<int:user_id>")
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    try:
        db.session.commit()
        flash("User deleted successfully!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Error deleting user: {str(e)}", "error")
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

        existing_product = Product.query.filter((Product.name == name) | (Product.description == description)).first()
        if existing_product:
            flash("This product name or description already exists.", "error")
            return render_template("add_product.html")

        new_product = Product(name=name, description=description, type=product_type)
        db.session.add(new_product)
        try:
            db.session.commit()
            flash("Product created successfully!", "success")
            # Render the same page with a success flag
            return render_template("add_product.html", success=True)
        except Exception as e:
            db.session.rollback()
            flash(f"Error adding product: {str(e)}", "error")
            return render_template("add_product.html")

    return render_template("add_product.html")


@app.route("/edit_product/<int:product_id>", methods=["GET", "POST"])
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    if request.method == "POST":
        product.name = request.form.get("name")
        product.description = request.form.get("description")
        product.type = request.form.get("type")

        db.session.add(product)
        db.session.commit()
        flash("Product updated successfully!", "success")
        return redirect(url_for("product", success=True))
    return render_template("edit_product.html", product=product )


@app.route("/delete_product/<int:product_id>")
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    try:
        db.session.commit()
        flash("Product deleted successfully!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Error deleting product: {str(e)}", "error")
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

        if not first_name or not last_name or not email or not product_id or not account_type or not currency:
            flash('All fields are required.', 'error')
            return render_template('add_account.html', products=products)
        
        existing_account = Account.query.filter_by(email=email).first()
        if existing_account:
            flash('An account with this email already exists.', 'error')
            return render_template('add_account.html', products=products)
        
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
        db.session.commit()
        flash('Account created successfully!', 'success')
        return render_template('add_account.html', products=products, success=True)
    
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
        db.session.add(account)
        db.session.commit()
        flash('Account updated successfully!', 'success')
        return redirect(url_for('account', success=True))
    
    return render_template('edit_account.html', account=account, products=products)


@app.route('/delete_account/<int:account_id>')
def delete_account(account_id):
    account = Account.query.get_or_404(account_id)
    db.session.delete(account)
    try:
        db.session.commit()
        flash('Account deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting account: {str(e)}', 'error')
    return redirect(url_for('account'))


@app.route('/account_search')
def account_search():
    query = request.args.get('query', '')
    accounts = Account.query.filter(
        (Account.first_name.ilike(f'%{query}%')) |
        (Account.last_name.ilike(f'%{query}%')) |
        (Account.email.ilike(f'%{query}%')) |
        (Account.phone_number.ilike(f'%{query}%')) |
        (Account.account_type.ilike(f'%{query}%')) |
        (Account.currency.ilike(f'%{query}%'))
    ).all()
    return render_template('account.html', accounts=accounts)


@app.route("/ad_group")
def ad_group():
    ad_groups = list(Group.query.order_by(Group.name).all())
    print("Number of groups fetched:", len(ad_groups))  # This will show you how many groups are fetched
    return render_template("ad_group.html", ad_groups=ad_groups)


@app.route("/add_ad_group", methods=["GET", "POST"])
def add_ad_group():
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        group_type = request.form.get("group_type")

        if not name or not description or not group_type:
            flash("All fields are required.", "error")
            return render_template("add_ad_group.html")

        existing_group = Group.query.filter_by(name=name).first()
        if existing_group:
            flash("A group with this name already exists.", "error")
            return render_template("add_ad_group.html")

        new_group = Group(name=name, description=description, group_type=group_type)
        db.session.add(new_group)
        db.session.commit()
        flash("AD group created successfully!", "success")
        return render_template("add_ad_group.html", success=True)  # Note the 'success=True'

    return render_template("add_ad_group.html")


@app.route("/edit_ad_group/<int:group_id>", methods=["GET", "POST"])
def edit_ad_group(group_id):
    group = Group.query.get_or_404(group_id)
    if request.method == "POST":
        group.name = request.form.get("name")
        group.description = request.form.get("description")
        group.group_type = request.form.get("group_type")

        db.session.add(group)
        db.session.commit()
        flash("Group updated successfully!", "success")
        return redirect(url_for("ad_group", success=True))
    return render_template("edit_ad_group.html", group=group)


@app.route("/delete_ad_group/<int:group_id>")
def delete_ad_group(group_id):
    group = Group.query.get_or_404(group_id)
    db.session.delete(group)
    try:
        db.session.commit()
        flash("Group deleted successfully!", "success")

    except Exception as e:
        db.session.rollback()
        flash(f"Error deleting group: {str(e)}", "error")

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

        if not headline or not description:
            flash("All fields are required.", "error")
            return render_template("add_news.html")
        
        existing_news_item = NewsItem.query.filter_by(headline=headline).first()
        if existing_news_item:
            flash("A news item with this headline already exists.", "error")
            return render_template("add_news.html")
        
        news_item = NewsItem(headline=headline, description=description)
        db.session.add(news_item)
        db.session.commit()
        flash("News item created successfully!", "success")
        return render_template("add_news.html", success=True)
    
    return render_template("add_news.html")


@app.route('/edit_news/<int:news_id>', methods=["GET", "POST"])
def edit_news(news_id):
    news_item = NewsItem.query.get_or_404(news_id)
    if request.method == "POST":
        news_item.headline = request.form.get("headline")
        news_item.description = request.form.get("description")
        
        db.session.add(news_item)
        db.session.commit()
        flash("News item updated successfully!", "success")
        return redirect(url_for("news", success=True))

    news_items = NewsItem.query.all()  # This will fetch all news items for listing
    return render_template("edit_news.html", news_item=news_item, news_items=news_items)


@app.route('/delete_news/<int:news_id>')
def delete_news(news_id):
    news_item = NewsItem.query.get_or_404(news_id)
    db.session.delete(news_item)

    try:
        db.session.commit()
        flash("News item deleted successfully!", "success")
    except Exception as e:
        db.session.rollback()
        flash(f"Error deleting news item: {str(e)}", "error")

    return redirect(url_for("news"))


@app.route('/news_search')
def news_search():
    query = request.args.get('query', '')
    news_items = NewsItem.query.filter(
        (NewsItem.headline.ilike(f'%{query}%')) |
        (NewsItem.description.ilike(f'%{query}%'))
    ).all()
    return render_template('news.html', news_items=news_items)
