from flask_sqlalchemy import SQLAlchemy 
import os
import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)


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


class Users(db.Model):
    email = db.Column(db.String,  primary_key=True)
    password = db.Column(db.String, nullable=False)


    
