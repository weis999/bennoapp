from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash
import datetime

"""
A Document for MongoDB, so that users cannot add other fields then what are 
defined here. 
- Name: is a field of type 'STRING', with two constraints 'REQUIRED' and 'UNIQUE' 
  - The constraint 'REQUIRED' means the user cannot create a new movie without 
    giving its title.
  - The constraint 'UNIQUE' means the movie name must be unique and cannot be repeated
- Casts: is a field of type 'LIST' which contains the value of type 'STRING'.
"""

# Document Result_progress, with fields and constraints
class Result_progress(db.Document):
    lenght_p = db.DecimalField(required=False)
    weight_p = db.DecimalField(required=False)
    added_by = db.ReferenceField('Person')

# Document 'Person' and with fields and constraints 'required' 'min_length', 'max_length', 'unique'
class Person(db.Document):
    firstname = db.StringField(required=True)
    lastname = db.StringField(required=True)
    geslacht = db.StringField(required=False, min_lengt=3, max_length=6)
    address = db.StringField(required=True)
    zipcode = db.StringField(required=True, min_length=6, max_length=6, unique=True)
    city = db.StringField(required=True)
    telnr = db.StringField(required=True, min_length=10, max_length=10, unique=True)
    birthday = db.StringField(required=True, min_length=8)
    email = db.EmailField(required=True, unique=True)
    password = db.StringField(required=True, min_length=6)
    results = db.ListField(db.ReferenceField('Result_progress', reverse_delete_rule=db.PULL))

   # Method for hashing the password
    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    # Method for checking if the password used by the user to login generates
    # the hash which is equal to the password saved in the database check_password_hash()
    def check_password(self, password):
        return check_password_hash(self.password, password)
        
Person.register_delete_rule(Result_progress, 'added_by', db.CASCADE)
