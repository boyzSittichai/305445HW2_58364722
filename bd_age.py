from flask import Flask , request
from flask_restful import Resource ,Api,reqparse
import json,time
from datetime import datetime,date
from werkzeug.datastructures import FileStorage

app = Flask (__name__)

api = Api(app)

def calculate_myage(born):
	today = date.today()
	return today.year-born.year-((today.month, today.day) < (born.month, born.day))

parser = reqparse.RequestParser()
parser.add_argument('birthday')
#parser.add_argument('image', type=FileStorage, location='files')

class Home(Resource):
	def get(self):
		return {"information":"'./birthday' to calculate age or './image' to upload image/picture/photo "}

class Birthday(Resource):
	def get(self):
		return {"information":"Plese sent 'My birthday' (POST method)"}
	def post(self):
		args = parser.parse_args()
		birthdate = args['birthday']
		datetime_object = datetime.strptime(birthdate, '%d-%m-%Y')
		age = int(calculate_myage(datetime_object))
		return {"birthday":birthdate,"age":age}

api.add_resource(Home,'/')
api.add_resource(Birthday,'/birthday')
#api.add_resource(Image,'/image')
if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5100)
