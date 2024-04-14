from accountsphere import db
from datetime import datetime


class User(db.Model):
    # This class is a model for the users table in the database
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False) 
    last_name = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(120), unique=True, nullable=False)
    role = db.Column(db.String(50), nullable=False)
    groups = db.relationship('Group', secondary='user_groups', back_populates="users")
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        # This method returns a string representation of the object
        return f'<User {self.username}>'


class Group(db.Model):
    # This class is a model for the groups table in the database
    __tablename__ = 'groups'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    group_type = db.Column(db.String(50), nullable=False)  # Added to capture group type (Security, Distribution)
    users = db.relationship('User', secondary='user_groups', back_populates="groups")

    def __repr__(self):
        # This method returns a string representation of the object
        return f'<Group {self.name}>'


class UserGroup(db.Model):
    # This class is a model for the user_groups table in the database
    __tablename__ = 'user_groups'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey('groups.id'), primary_key=True)
    role_within_group = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        # This method returns a string representation of the object
        return f'<UserGroup user_id={self.user_id}, group_id={self.group_id}>'

class Customer(db.Model):
    # This class is a model for the customers table in the database
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(20), unique=True, nullable=True)
    date_of_birth = db.Column(db.Date, nullable=True) 
    accounts = db.relationship('Account', backref='customer', lazy=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        # This method returns a string representation of the object
        return f'<Customer {self.first_name} {self.last_name}>'


class Product(db.Model):
    # This class is a model for the products table in the database
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    type = db.Column(db.String(50), nullable=False)
    accounts = db.relationship('Account', backref='product', lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        # This method returns a string representation of the object
        return f'<Product {self.name}>'

class Account(db.Model):
    # This class is a model for the accounts table in the database
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    balance = db.Column(db.Numeric(10, 2), default=0.00)
    currency = db.Column(db.String(3), nullable=False, default='USD') 
    status = db.Column(db.String(20), default='active')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        # This method returns a string representation of the object
        return f'<Account {self.id}>'
