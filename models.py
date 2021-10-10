from flask.app import Flask
from flask_sqlalchemy import SQLAlchemy 
import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)



# DATABASE_URL  = 'postgresql://mohamed:123@127.0.0.1:5432/shoping'

print('database url ---------> ', DATABASE_URL)

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

db = SQLAlchemy()

def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
    return db

'''
Customers
	id (pr), first_name , last_name , address , phone_number , total_cart


Cart items :
	id (pr), quantity,  product_id (fk), customer_id (fk)


Categories:
	id (pr), category_name

Products :
	id (pr), product_name  , category (fk)


'''
# class Category(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     category_name = db.Column(db.String, nullable=False)
#     products = db.relationship('Product', backref='products')

# class Product(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     product_name = db.Column(db.String, nullable=False)    
#     products = db.relationship('cart_item', backref='items')
#     category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)

# class Customer(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     first_name = db.Column(db.String, nullable=False)
#     last_name = db.Column(db.String, nullable=False)
#     address = db.Column(db.String, nullable=False)
#     phone = db.Column(db.String, nullable=False)
#     total_price = db.Column(db.Float)    
#     customers = db.relationship('cart_item', backref='customer')

# class CartItem(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     quantity = db.Column(db.Integer)
#     ## foreign keys
#     product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
#     customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    
    

class Users(db.Model):
    email = db.Column(db.String,  primary_key=True)
    password = db.Column(db.String, nullable=False)


    