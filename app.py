"""
   Module-Flask: For our web server.
   * Function-request: ...
   * Function-Response: To set the type of a response
   Module-database.db: Self made module in ~/movie-bag/database/
   * initialize_db: This function is to intialize the database
   Module-database.models:  Self made module in ~/movie-bag/database/
   * Function-Movie: This is a function to make a document into the database
"""
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from resources.errors import errors
from database.db import initialize_db
from flask_restful import Api
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


app = Flask(__name__)
app.config.from_envvar('ENV_FILE_LOCATION')
# In this app the following CRUDs are being used: 'CREATE', 'UPDATE', 'GET', 'DELETE'
api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Configuration for our mongodb database: 'HOST' + format '<host-url>/<database-name>'
# The <database-name> will be used for the name of the newly created database
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://weis999:68Y3bgxfbm12CmxMLVx1iPDndecXSzZFayQ8hY9NfOvfUq7Pey3HI2l6V0Y4IAca9WNIq11VZzxiqahJAnoITA==@weis999.mongo.cosmos.azure.com:10255/benno_01?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@weis999@'
}
#app.config['MONGO_HOST'] = 'weis999.mongo.cosmos.azure.com' # host URI
#app.config['MONGO_PORT'] = 10255
#app.config['MONGO_DBNAME'] = 'benno_02'
#app.config['MONGO_USERNAME'] = 'weis999'
#app.config['MONGO_PASSWORD'] = '68Y3bgxfbm12CmxMLVx1iPDndecXSzZFayQ8hY9NfOvfUq7Pey3HI2l6V0Y4IAca9WNIq11VZzxiqahJAnoITA=='
#app.config['MONGO_OPTIONS'] = 'ssl=true&retrywrites=false&ssl_cert_reqs=CERT_NONE'

# The database will be here initialized!
initialize_db(app)
# The routes will be here initialized!
initialize_routes(api)


if __name__ == '__main__':
    # With the app.run the flask server will be called into action
    app.run(debug=True, host='0.0.0.0', port='80', ssl=True)
