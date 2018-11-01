import flask
from flask import request, jsonify

# Creación de una nueva aplicación web
app = flask.Flask(__name__)

#Esta API está hecha con una pequeña cantidad de datos contenida en la siguiente lista:
#Para efecto de hacer esta tarea: estos datos son de un juego, ya que por desgracia, los casos de uso hechos en la tarea anterior no los tengo. 
naves = [
	{'id':0,
	'name': 'Malediction',
	'size':'small',
	'Role':'Interceptor',
	'M-Weapons':'lasers', #M-Weapons = Main Weapons
	'M-Defense':'armor'}, #M-Defense = Main Defense
	{'id':1,
	'name': 'Ares',
	'size':'small',
	'Role':'Interceptor',
	'M-Weapons':'blasters',
	'M-Defense':'armor'},
	{'id':2,
	'name': 'Stiletto',
	'size':'small',
	'Role':'Interceptor',
	'M-Weapons':'artillery',
	'M-Defense':'shield'},
	{'id':3,
	'name': 'Taranis',
	'size':'small',
	'Role':'Interceptor',
	'M-Weapons':'blasters',
	'M-Defense':'armor'},
	{'id':4,
	'name': 'Enyo',
	'size':'small',
	'Role':'Assault Frigate',
	'M-Weapons':'blasters',
	'M-Defense':'armor'},
	{'id':5,
	'name': 'Retribution',
	'size':'small',
	'Role':'Assault Frigate',
	'M-Weapons':'lasers',
	'M-Defense':'armor'},
]

# Definición de las rutas

@app.route('/', methods=['GET'])
def home():
	return "<h1>Intento de API de EVE online<h1><h2>Esta api contiene solo unas poquitas naves de tamaño pequeño de el juego EVE online<h2>"
@app.route('/api_EVE/v1/resources/naves', methods=['GET'])
def api_filter_naves():
	parameters = request.args
	ID_b=True
	if 'id' in parameters:
		id_nave = int(parameters.get('id'))
	else: ID_b=False ##Este booleano, indica que no esta id en la consulta
	role = parameters.get('role')
	weapon = parameters.get('weapon')
	defense = parameters.get('defense')
	result=[]
	print("role: ",role)
	print("weapon: ",weapon)
	print("defense: ",defense)
	if ID_b:
		for nave in naves:
			if nave['id'] == id_nave or nave['Role'] == role or nave['M-Weapons'] == weapon or nave['M-Defense'] == defense: result.append(nave) 
	else:
		for nave in naves:
			if nave['Role'] == role or nave['M-Weapons'] == weapon or nave['M-Defense'] == defense: result.append(nave) 
		
	return jsonify(result)

@app.route('/api_EVE/v1/resources/naves/all', methods=['GET'])
def api_naves_all():
	return jsonify(naves)
app.run(debug=False,port=1234)
