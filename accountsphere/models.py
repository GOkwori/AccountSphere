from accountsphere import db
from flask_login import UserMixin, AnonymousUserMixin
from datetime import datetime


# Define the User model
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(256))
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(50), nullable=False)
    active = db.Column(db.Boolean, default=True)
    group_id = db.Column(db.Integer, db.ForeignKey(
        'groups.id'), nullable=True)  # ForeignKey linking to Group
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(
    ), onupdate=db.func.current_timestamp())

    def get_id(self):
        return str(self.id)

    @property
    def is_active(self):
        return self.active
    
    def is_administrator(self):
        return self.role == 'administrator'
    
    def is_account_officer(self):
        return self.role == 'account officer'
    
    def is_product_manager(self):
        return self.role == 'product manager'
    
    def is_news_analyst(self):
        return self.role == 'news analyst'

# Define the AnonymousUser model
class AnonymousUser(AnonymousUserMixin):
    def is_administrator(self):
        return False

    def is_account_officer(self):
        return False

    def is_product_manager(self):
        return False

    def is_news_analyst(self):
        return False
    

# Define the Group model
class Group(db.Model):
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text)
    group_type = db.Column(db.String(50), nullable=False)
    # Relationship with dynamic loading
    users = db.relationship('User', backref='group',
                            cascade='all, delete', lazy='dynamic')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(
    ), onupdate=db.func.current_timestamp())

    def __repr__(self):
        return f'<Group {self.name}>'


#  Define the Product model
class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    type = db.Column(db.String(50), nullable=False)
    accounts = db.relationship(
        'Account', backref='product', cascade='all, delete', lazy=True)

    def __repr__(self):
        return f'<Product {self.name}>'


# Define the Account model
class Account(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), unique=True, nullable=True)
    date_of_birth = db.Column(db.Date, nullable=True)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'products.id', ondelete='CASCADE'), nullable=False)
    account_type = db.Column(db.String(50), nullable=False)
    balance = db.Column(db.Numeric(10, 2), default=0.00)
    currency = db.Column(db.String(3), nullable=False, default='USD')
    status = db.Column(db.String(20), default='active')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(
    ), onupdate=db.func.current_timestamp())

    def __repr__(self):
        return f'<Account {self.first_name} {self.last_name} | Account ID:{self.id}>'


# Define the Transaction model
class NewsItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    headline = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<NewsItem {self.headline}>'
