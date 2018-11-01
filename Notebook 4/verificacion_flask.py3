import flask
from flask import request,jsonify

app = flask.Flask(__name__)

# Create some test data for our catalog in the form of a list of dictionaries.
naves=[
	{'id':0,
	'nombre':'Malediction',
	'clase':'Interceptor',
	'tamaño':'pequeña'},
	{'id':1,
	'nombre':'Enyo',
	'clase':'Fraga de Asalto',
	'tamaño':'pequeña'},	
]


@app.route('/', methods=['GET'])
def home():
    return "<h1>¡Hola Mundo!</h1> <p>Bienvenido en nuestra aplicación web básica en Python</p>"

# A route to return all of the available entries in our catalog.
@app.route('/api/v1/resources/naves/all', methods=['GET'])
def api_all():
	if 'id' in request.args:
		id = int(request.args['id'])
		results=[]
		for nave in naves:
			if(nave['id'] == id): results.append(nave)
		return jsonify(results)
	else: return jsonify(naves)
    	
if __name__ == "__main__":
	app.run(debug=False,port=1234)
