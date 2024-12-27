# basic configuration

# imports flask frameowrk to create a web server
from flask import Flask 
# adds a database system (SQLite) for storing data
from flask_sqlalchemy import SQLAlchemy 
# cross origin request, allows us to send a request to this backend from a different URL, the frontend (REACT, HTML, etc) and backend can communicate even if they're running on different servers or ports
from flask_cors import CORS 

# frontend is a different server than the backend

# initializes flask application, creates the flask app object, central controller of your web app
app = Flask(__name__) 

# disables cors error so we can send cross origin requests to app
CORS(app)

# initalizes database, specifiyng the location of the local SQL lite database that we are going to be storing on our machine, essentially storing a file
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"

# not going to track all the modifications we make to the database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# creating an instance of the database and pass app object, gives us access to the database so we can create modify etc
db = SQLAlchemy(app)

