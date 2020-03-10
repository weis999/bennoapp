"""
   Module-Flask: For our web server.
   * Function-request: ...
   * Function-Response: To set the type of a response
   Module-database.db: Self made module in
   * initialize_db: This function is to intialize the database
   Module-database.models:  Self made module in ~/movie-bag/database/
   * Function-Movie: This is a function to make a document into the database
"""
from flask import Flask
from flask_restful import Api
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from resources.errors import errors
from database.db import initialize_db
from resources.routes import initialize_routes

""" 
 @@ POSTMAN @@
 To test our environment we will be using Postman application. Post man is used for
 testing the APIs with different HTTP-methods. Such as sending data to our Flask
 server with 'POST' request, updating the data into our Flask server with 'PUT'
 request, getting the data from the flask server with 'GET' and deleting them with
 'DELETE' request. This is the url for POSTMAN: https://www.postman.com/downloads/
 @@ POSTMAN @@
"""

# In this app the following CRUDs are being used: 'CREATE', 'UPDATE', 'GET', 'DELETE'
app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')
api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Configuration for our mongodb database: 'HOST' + format '<host-url>/<database-name>'
# The <database-name> will be used for the name of the newly created database
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/benno_01'
}

# The database will be here initialized!
initialize_db(app)
# The routes will be here initialized!
initialize_routes(api)


# Run the app on port 5000 on all interfaces, accepting only HTTPS connections
if __name__ == '__main__':
    app.run(debug=True, ssl_context='adhoc', host='0.0.0.0', port=5000)