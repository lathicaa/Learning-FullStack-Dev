# NOTES
# figure out what are the different endpoints or routes that i want for my API to access and create diff resources etc
# want a CRUD app (create, read, update, delete)

# create
# - first_name
# - last_name
# - email

# when we create an API, we have some sort of server that is running the API, the server has some kind of address, this is the domain or servers URL
# an endpoint is anything that comes after this domain
# localhost:5000/create_contact (create_contact is the endpoint)

# a request is anything we send to any server in our case an API, have diff types
# get request is trying to access some type of resource
# post request is trying to create something new
# patch request is trying to update something
# delete request is to delete
# another piece of data we can send is JSON data, information that comes alongside our request that is used when we are handling our request to do something
# the front end is going to send a request to our backend and the back end is going to return a response

# response will contain:
# - status: will tell if request was successful
# - can also return some json

# we have these diff endpoints, just code written in python, they handle a request that will come from an external source (the frontend or the website), then our API will return a response which will contain how that request was handled
# we are building this API
# defines routes that the frontend interacts with 

# The flask provides a RESTful API with CRUD operations
# It stores data in an SQLite database
# The frontend can interact with backend using HTTP requests (get, post, patch, delete)


# -- START CODE --

# jsonify allows us to return json data
from flask import request, jsonify
from config import app, db
from models import Contact

# route to create a contact
# decorater, inside of here, specify what route we are going to go to, then specify the valid methods, 
# query all the contacts, convert them into json, then return them
# /contacts fetches all contacts when you send a GET request
@app.route("/contacts", methods = ["GET"])
def get_contacts():

    # uses FlaskSQLAlchemy to get all the diff contacts that exist inside of the databse
    contacts = Contact.query.all() 

    # need to convert python data to json
    json_contacts = list(map(lambda x: x.to_json(), contacts))

    # the above maps each contact object to its JSON representation using the to_json() method
    return jsonify({"contacts": json_contacts}) #sends the contacts back to the frontend in JSON format


# route to create contacts
@app.route("/create_contact", methods = ["POST"])
def create_contact():

    # look at json data and make sure its valid to create a contact, extracts data sent in the request body as JSON
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email") 

    if not first_name or not last_name or not email:
        return (
            jsonify({"message": "You must include a first name, last name, and email"}), 
            400,
        )

    # when we want to add a new entry to our database we create the python class corresponding to that entry
    # creates a new database entry and commits it
    new_contact = Contact(first_name = first_name, last_name = last_name, email = email)
    try:
        db.session.add(new_contact) # then add it to our data base
        db.session.commit() # then commit it and write it into the database permanently, errors can occur during this so we put it in a try and except block  
    except Exception as e:
        return jsonify({"message": str(e)}), 400 # this is to deal with the errors

    return jsonify({"message": "User created!"}), 201


# route to update contact
@app.route("/update_contact/<int:user_id>", methods = ["PATCH"])
def update_contact(user_id):

    # look in contact database and find user that has this ID
    contact = Contact.query.get(user_id) 

    if not contact:
        return jsonify({"message": "User not found"}), 404


    # modify this contacts fisrt name to be equal to whatever json data first name is that was given to us, otherwise leave it as whatever it was
    data = request.json
    contact.first_name = data.get("firstName", contact.first_name) 
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)

    db.session.commit()

    return jsonify({"message": "User Updated!"}), 200


# route to delete contacts
@app.route("/delete_contact/<int:user_id>", methods = ["DELETE"])
def delete_contact(user_id):

    # look in contact database and find user that has this ID
    contact = Contact.query.get(user_id) 

    if not contact:
        return jsonify({"message": "User not found"}), 404

    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "User deleted!"}), 200


# need to run flask application
if __name__ == "__main__":

    # need to instantiate our database
    with app.app_context():

        # go ahead and create all the diff models we have to find in our database, creates database tables if they don't already exist
        db.create_all() 

    # start running the code, starts running the diff endpoints and our API
    app.run(debug = True) 



