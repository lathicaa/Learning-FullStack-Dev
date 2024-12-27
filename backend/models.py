# database models - defines the structure of database using python classes
# this is going to be a database model represented as a python class, in python code we know define the diff field this obejct will have
# Contact Model - defines a table called Contact with columns
    # - id: primary key (unique identifier)
    # - first_name, last_name, email - user provided fields with contraints such as u have to have unique email


# import the db variable, this instance gives us access to SQLAlchemy
from config import db


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True) # always need to have an id for all database instances
    first_name = db.Column(db.String(80), unique = False, nullable = False)
    last_name = db.Column(db.String(80), unique = False, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)

    # function to take all the diff fields we have on our object and convert it into a python dictionary to then convert into json which is something we can pass to our API
    # when we build an api, the way we communicate is through JSON (javascript object notation), passing JSON back and forth so api will return JSON, and we will send JSON to the API to create our different objects
    # you have  these diff fields ur storing in ur contact, want to convert them all to this JSON object so its easy for you to take a contact and give it to the frontend or anyone requesting to get our diff contacts
    # this function converts the Contact object into a JSON formt so it can be sent to the frontend as a response
    def to_json(self):
        return{
            # for JSON code use camel case notation for fields, snake case for python
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
        }

        # self parameter refers to the specific contact object, it acts as a reference to the curent object calling the method