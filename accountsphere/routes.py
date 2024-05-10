from flask import render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from accountsphere import app, db
from accountsphere.models import User, Group, Product, Account, NewsItem
from sqlalchemy.orm import joinedload
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy import or_


# Function to verify user role(s)
def has_any_role(*roles):
    """Check if the current user has any of the given roles."""
    if not current_user.is_authenticated:
        return False
    # Convert the current user's roles into a list of lowercase strings
    user_roles = [role.strip().lower() for role in current_user.role.split(',')]
    # Check if any of the given roles match the user's roles
    return any(role.lower() in user_roles for role in roles)


# Define the home route
@app.route("/")
def home():
    return render_template("landing.html")


# Define the register route
@app.route("/register", methods=["GET", "POST"])
def register():
    groups = Group.query.all()
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if User.query.filter_by(username=username).first():
            flash("Username already exists.", "error")
            return render_template("register.html", groups=groups)

        if User.query.filter_by(email=email).first():
            flash("Email already exists.", "error")
            return render_template("register.html", groups=groups)

        if password != confirm_password:
            flash("Passwords do not match.", "error")
            return render_template("register.html", groups=groups)

        new_user = User(
            first_name=request.form.get("first_name"),
            last_name=request.form.get("last_name"),
            username=username,
            email=email,
            password_hash=generate_password_hash(password),
            role=request.form.get("role")
        )
        db.session.add(new_user)
        db.session.commit()
        flash("Account created successfully", 'success')
        return redirect(url_for('login'))

    return render_template("register.html", groups=groups)


# Define the login route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('profile'))
        else:
            flash('Invalid username or password.', 'error')
    return render_template("login.html")


# Define the logout route
@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for("home"))


# Define the password reset route
@app.route('/password_reset', methods=['GET', 'POST'])
@login_required
def password_reset():
    if request.method == 'POST':
        old_password = request.form.get('old_password')
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')

        if not check_password_hash(current_user.password_hash, old_password):
            flash('Old password is incorrect.', 'error')
            return redirect(url_for('password_reset'))

        if new_password != confirm_password:
            flash('New passwords do not match.', 'error')
            return redirect(url_for('password_reset'))

        if check_password_hash(current_user.password_hash, new_password):
            flash('New password must be different from the old password.', 'error')
            return redirect(url_for('password_reset'))

        current_user.password_hash = generate_password_hash(new_password)
        db.session.commit()
        flash('Your password has been updated successfully!', 'success')
        return redirect(url_for('profile'))

    return render_template('password_reset.html')


# Define the profile route
@app.route("/profile")
@login_required
def profile():
    news_items = NewsItem.query.all()
    return render_template('index.html', news_items=news_items)


# Define the account route
@app.route("/account")
@login_required
def account():
    if not has_any_role('administrator', 'account officer'):
        flash("You do not have permission to view this page.", 'error')
        return redirect(url_for('profile'))

    accounts = Account.query.options(joinedload(Account.product))\
        .order_by(Account.first_name, Account.last_name).all()
    return render_template("account.html", accounts=accounts)


# Define the add account route
@app.route('/add_account', methods=['GET', 'POST'])
@login_required
def add_account():
    if not has_any_role('administrator', 'account officer'):
        flash("You do not have permission to view this page.", 'error')
        return redirect(url_for('profile'))

    products = Product.query.order_by(Product.name.asc()).all()

    if request.method == 'POST':
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
            status='active'
        )

        db.session.add(account)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('account'))

    return render_template('add_account.html', products=products)


# Define the edit account route
@app.route('/edit_account/<int:account_id>', methods=['GET', 'POST'])
@login_required
def edit_account(account_id):
    if not has_any_role('administrator', 'account officer'):
        flash("You do not have permission to edit this item.", 'error')
        return redirect(url_for('profile'))

    account = Account.query.get_or_404(account_id)
    products = Product.query.all()
    if request.method == 'POST':
        account.first_name = request.form.get('first_name')
        account.last_name = request.form.get('last_name')
        account.email = request.form.get('email')
        account.phone_number = request.form.get('phone_number')
        account.date_of_birth = request.form.get('date_of_birth')
        account.product_id = request.form.get('product_id')
        account.account_type = request.form.get('account_type')
        account.balance = request.form.get('balance') or 0.00
        account.currency = request.form.get('currency')

        db.session.add(account)
        db.session.commit()
        flash('Account updated successfully!', 'success')
        return redirect(url_for('account', success=True))

    return render_template('edit_account.html', account=account, products=products)


# Define the delete account route
@app.route('/delete_account/<int:account_id>')
@login_required
def delete_account(account_id):
    if not has_any_role('administrator'):
        flash("You do not have permission to delete this item.", 'error')
        return redirect(url_for('profile'))

    account = Account.query.get_or_404(account_id)
    db.session.delete(account)
    try:
        db.session.commit()
        flash('Account deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting account: {str(e)}', 'error')
    return redirect(url_for('account'))


# Define the account search route
@app.route('/account_search')
@login_required
def account_search():
    if not has_any_role('administrator', 'account officer'):
        flash("You do not have permission to view this page.", 'error')
        return redirect(url_for('profile'))

    query = request.args.get('query', '').strip()

    if not query:
        return redirect(url_for('account'))

    accounts = Account.query.filter(
        or_(
            Account.first_name.ilike(f'%{query}%'),
            Account.last_name.ilike(f'%{query}%'),
            Account.email.ilike(f'%{query}%'),
            Account.phone_number.ilike(f'%{query}%'),
            Account.account_type.ilike(f'%{query}%'),
            Account.currency.ilike(f'%{query}%')
        )
    ).all()

    return render_template('account.html', accounts=accounts)


# Define the group route
@app.route("/ad_group")
@login_required
def ad_group():

    if not has_any_role('administrator'):
        flash("You do not have permission to view this page.", 'error')
        return redirect(url_for('profile'))

    # Fetch all groups and sort them by name
    ad_groups = list(Group.query.order_by(Group.name).all())
    # This will show you how many groups are fetched
    print("Number of groups fetched:", len(ad_groups))
    return render_template("ad_group.html", ad_groups=ad_groups)


@app.route("/add_ad_group", methods=["GET", "POST"])
@login_required
def add_ad_group():

    if not has_any_role('administrator'):
        flash("You do not have permission to view this page.", 'error')
        return redirect(url_for('profile'))
    
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        group_type = request.form.get("group_type")

        if not name or not description or not group_type:
            flash("All fields are required.")
            return render_template("add_ad_group.html")

        existing_group = Group.query.filter_by(name=name).first()
        if existing_group:
            flash("An AD-Group with this name already exists.")
            return render_template("add_ad_group.html")

        new_group = Group(name=name, description=description,
                          group_type=group_type)
        db.session.add(new_group)
        db.session.commit()
        flash("AD-Group created successfully!")
        # Note the 'success=True'
        return redirect(url_for("ad_group", success=True))

    return render_template("add_ad_group.html")


# Define the edit ad group route
@app.route("/edit_ad_group/<int:group_id>", methods=["GET", "POST"])
@login_required
def edit_ad_group(group_id):

    if not has_any_role('administrator'):
        flash("You do not have permission to edit this item.", 'error')
        return redirect(url_for('profile'))
    
    group = Group.query.get_or_404(group_id)
    if request.method == "POST":
        group.name = request.form.get("name")
        group.description = request.form.get("description")
        group.group_type = request.form.get("group_type")

        db.session.add(group)
        db.session.commit()
        flash("AD-Group updated successfully!")
        return redirect(url_for("ad_group", success=True))
    return render_template("edit_ad_group.html", group=group)


# Define the delete ad group route
@app.route("/delete_ad_group/<int:group_id>")
@login_required
def delete_ad_group(group_id):

    if not has_any_role('administrator'):
        flash("You do not have permission to delete this item.", 'error')
        return redirect(url_for('profile'))
    
    group = Group.query.get_or_404(group_id)
    db.session.delete(group)
    try:
        db.session.commit()
        flash("AD-Group deleted successfully!")

    except Exception as e:
        db.session.rollback()
        flash(f"Error deleting group: {str(e)}")

    return redirect(url_for("ad_group"))


# Define the ad group search route
@app.route("/ad_group_search")
@login_required
def ad_group_search():

    if not has_any_role('administrator'):
        flash("You do not have permission to view this page.", 'error')
        return redirect(url_for('profile'))
    
    query = request.args.get('query', '').strip()

    if query:
        ad_groups = Group.query.filter(
            or_(
                Group.name.ilike(f'%{query}%'),
                Group.description.ilike(f'%{query}%'),
                Group.group_type.ilike(f'%{query}%')
            )
        ).all()
    else:
        ad_groups = []

    return render_template('ad_group.html', ad_groups=ad_groups, query=query)


# Define the news route
@app.route("/news")
@login_required
def news():

    if not has_any_role('administrator', 'news analyst'):
        flash("You do not have permission to view this page.", 'error')
        return redirect(url_for('profile'))
    
    news_items = NewsItem.query.all()
    return render_template("news.html", news_items=news_items)


# Define the add news route
@app.route('/add_news', methods=["GET", "POST"])
@login_required
def add_news():

    if not has_any_role('administrator', 'news analyst'):
        flash("You do not have permission to view this page.", 'error')
        return redirect(url_for('profile'))
    
    if request.method == "POST":
        headline = request.form.get("headline")
        description = request.form.get("description")

        if not headline or not description:
            flash("All fields are required.")
            return render_template("add_news.html")

        existing_news_item = NewsItem.query.filter_by(
            headline=headline).first()
        if existing_news_item:
            flash("A news item with this headline already exists.")
            return render_template("add_news.html")

        news_item = NewsItem(headline=headline, description=description)
        db.session.add(news_item)
        db.session.commit()
        flash("News item created successfully!")
        return redirect(url_for("news", success=True))

    return render_template("add_news.html")


# Define the edit news route
@app.route('/edit_news/<int:news_id>', methods=["GET", "POST"])
@login_required
def edit_news(news_id):

    if not has_any_role('administrator', 'news analyst'):
        flash("You do not have permission to edit this item.", 'error')
        return redirect(url_for('profile'))
    
    news_item = NewsItem.query.get_or_404(news_id)
    if request.method == "POST":
        news_item.headline = request.form.get("headline")
        news_item.description = request.form.get("description")

        db.session.add(news_item)
        db.session.commit()
        flash("News item updated successfully!")
        return redirect(url_for("news", success=True))

    news_items = NewsItem.query.all()
    return render_template("edit_news.html", news_item=news_item,
                           news_items=news_items)


# Define the delete news route
@app.route('/delete_news/<int:news_id>')
@login_required
def delete_news(news_id):

    if not has_any_role('administrator', 'news analyst'):
        flash("You do not have permission to delete this item.", 'error')
        return redirect(url_for('profile'))
    
    news_item = NewsItem.query.get_or_404(news_id)
    db.session.delete(news_item)

    try:
        db.session.commit()
        flash("News item deleted successfully!")
    except Exception as e:
        db.session.rollback()
        flash(f"Error deleting news item: {str(e)}")

    return redirect(url_for("news"))


# Define the news search route
@app.route('/news_search')
@login_required
def news_search():

    if not has_any_role('administrator', 'news analyst'):
        flash("You do not have permission to view this page.", 'error')
        return redirect(url_for('profile'))
    
    query = request.args.get('query', '').strip()

    if query:
        news_items = NewsItem.query.filter(
            or_(
                NewsItem.headline.ilike(f'%{query}%'),
                NewsItem.description.ilike(f'%{query}%')
            )
        ).all()
    else:
        news_items = []

    return render_template('news.html', news_items=news_items, query=query)


# Define the product route
@app.route("/product")
@login_required
def product():

    if not has_any_role('administrator', 'product manager'):
        flash("You do not have permission to view this page.", 'error')
        return redirect(url_for('profile'))
    
    products = list(Product.query.order_by(Product.name).all())
    print("Number of products fetched:", len(products))
    return render_template("product.html", products=products)


# Define the add product route
@app.route("/add_product", methods=["GET", "POST"])
@login_required
def add_product():

    if not has_any_role('administrator', 'product manager'):
        flash("You do not have permission to view this page.", 'error')
        return redirect(url_for('profile'))
    
    if request.method == "POST":
        name = request.form.get("name")
        description = request.form.get("description")
        product_type = request.form.get("type")

        existing_product = Product.query.filter(
            (Product.name == name) |
            (Product.description == description)).first()
        if existing_product:
            flash("This product name or description already exists.")
            return render_template("add_product.html")

        new_product = Product(
            name=name, description=description, type=product_type)
        db.session.add(new_product)
        try:
            db.session.commit()
            flash("Product created successfully!")
            # Render the same page with a success flag
            return redirect(url_for("product"))
        except Exception as e:
            db.session.rollback()
            flash(f"Error adding product: {str(e)}")
            return render_template("add_product.html")

    return render_template("add_product.html")


# Define the edit product route
@app.route("/edit_product/<int:product_id>", methods=["GET", "POST"])
@login_required
def edit_product(product_id):

    if not has_any_role('administrator', 'product manager'):
        flash("You do not have permission to edit this item.", 'error')
        return redirect(url_for('profile'))
    
    product = Product.query.get_or_404(product_id)
    if request.method == "POST":
        product.name = request.form.get("name")
        product.description = request.form.get("description")
        product.type = request.form.get("type")

        db.session.add(product)
        db.session.commit()
        flash("Product updated successfully!")
        return redirect(url_for("product", success=True))
    return render_template("edit_product.html", product=product)


# Define the delete product route
@app.route("/delete_product/<int:product_id>")
@login_required
def delete_product(product_id):

    if not has_any_role('administrator', 'product manager'):
        flash("You do not have permission to delete this item.", 'error')
        return redirect(url_for('profile'))
    
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    try:
        db.session.commit()
        flash("Product deleted successfully!")
    except Exception as e:
        db.session.rollback()
        flash(f"Error deleting product: {str(e)}")
    return redirect(url_for("product"))


# Define the product search route
@app.route("/product_search")
@login_required
def product_search():

    if not has_any_role('administrator', 'product manager'):
        flash("You do not have permission to view this page.", 'error')
        return redirect(url_for('profile'))
    
    query = request.args.get('query', '').strip()

    if query:
        products = Product.query.filter(
            or_(
                Product.name.ilike(f'%{query}%'),
                Product.description.ilike(f'%{query}%'),
                Product.type.ilike(f'%{query}%')
            )
        ).all()
    else:
        products = []

    return render_template('product.html', products=products, query=query)


# Define the user route
@app.route("/user")
@login_required
def user():

    if not has_any_role('administrator'):
        flash("You do not have permission to view this page.", 'error')
        return redirect(url_for('profile'))
    
    users = User.query.order_by(User.first_name, User.last_name).all()
    return render_template("user.html", users=users)


# Define the add user route
@app.route("/add_user", methods=["GET", "POST"])
@login_required
def add_user():
    if not has_any_role('administrator'):
        flash("You do not have permission to view this page.", 'error')
        return redirect(url_for('profile'))
    
    groups = Group.query.all()

    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")

        if User.query.filter_by(username=username).first():
            flash("Username already exists.")
            return render_template("add_user.html", groups=groups)
        if User.query.filter_by(email=email).first():
            flash("Email already exists.")
            return render_template("add_user.html", groups=groups)

        user = User(
            first_name=request.form.get("first_name"),
            last_name=request.form.get("last_name"),
            username=username,
            email=email,
            password_hash=generate_password_hash(request.form.get("password")),
            role=request.form.get("role")
        )
        db.session.add(user)
        db.session.commit()
        flash("User created successfully!")
        return redirect(url_for("user"))

    return render_template("add_user.html", groups=groups)


# Define the edit user route
@app.route("/edit_user/<int:user_id>", methods=["GET", "POST"])
@login_required
def edit_user(user_id):

    if not has_any_role('administrator'):
        flash("You do not have permission to edit this item.", 'error')
        return redirect(url_for('profile'))
    
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
        flash("User updated successfully!")
        return redirect(url_for("user"))

    return render_template("edit_user.html", user=user, groups=groups)


# Define the delete user route
@app.route("/delete_user/<int:user_id>")
@login_required
def delete_user(user_id):

    if not has_any_role('administrator'):
        flash("You do not have permission to delete this item.", 'error')
        return redirect(url_for('profile'))
    
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    try:
        db.session.commit()
        flash("User deleted successfully!")
    except Exception as e:
        db.session.rollback()
        flash(f"Error deleting user: {str(e)}")
    return redirect(url_for("user"))


# Define the user search route
@app.route("/user_search")
@login_required
def user_search():

    if not has_any_role('administrator'):
        flash("You do not have permission to view this page.", 'error')
        return redirect(url_for('profile'))
    
    query = request.args.get('query', '').strip()

    if query:
        users = User.query.filter(
            or_(
                User.first_name.ilike(f'%{query}%'),
                User.last_name.ilike(f'%{query}%'),
                User.username.ilike(f'%{query}%'),
                User.email.ilike(f'%{query}%')
            )
        ).all()
    else:
        users = []

    return render_template('user.html', users=users, query=query)


# Define the error handler for 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error_page=True), 404


# Define the error handler for 500
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error_page=True), 500
