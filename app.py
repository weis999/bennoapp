from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from resources.errors import errors
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes

app = Flask(__name__)
app.config['SECRET_KEY'] = 'nultjm2hoe0bioq32xohyt06bdrlp7'
api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://weis999:68Y3bgxfbm12CmxMLVx1iPDndecXSzZFayQ8hY9NfOvfUq7Pey3HI2l6V0Y4IAca9WNIq11VZzxiqahJAnoITA==@weis999.mongo.cosmos.azure.com:10255/benno_01?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@weis999@'
}
initialize_db(app)
initialize_routes(api)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
