from flask import Response, request
from flask_jwt_extended import create_access_token
from database.models import Person
from flask_restful import Resource
from mongoengine import FieldDoesNotExist, NotUniqueError, DoesNotExist
from resources.errors import SchemaValidationError, EmailAlreadyExistsError, UnauthorizedError, InternalServerError
import datetime

# Endpoint for '/api/v1/auth/signup/'
# Endpoint for 'POST' a data into the 'Person' document in database 'benno_01' 
class SignupApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            person =  Person(**body)
            person.hash_password()
            person.save()
            id = person.id
	    # hier nog invoer gegevens uitprinten++
            return {'id': str(id)}, 200
        except FieldDoesNotExist:
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        except Exception as error:
            raise InternalServerError

class SigninApi(Resource):
    # Method login
    def post(self):
        try:
            body = request.get_json()
            person = Person.objects.get(email=body.get('email'))
            authorized = person.check_password(body.get('password'))
            if not authorized:
                raise UnauthorizedError

            expires = datetime.timedelta(minutes=60)
            access_token = create_access_token(identity=str(person.id), expires_delta=expires)
            return {'token': access_token}, 200
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception as error:
            raise InternalServerError

class PersonGet(Resource):
	# Method for getting info_person from collection Person
    def get(self):
        query = Person.objects()
        results = Person.objects().to_json()
        return Response(results, mimetype="application/json", status=200)
