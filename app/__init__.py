from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__, instance_relative_config=False)
app.config['SECRET_KEY'] = 'c39f53dab6fa151e766c5325943c6e59b4783dd3c909b47568de52b6957921e8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mypassword@localhost/report'
db = SQLAlchemy(app)


# Import parts of our core Flask app
from app import routes