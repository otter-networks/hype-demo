#!/usr/bin/env python
import json
import flask
from flask import jsonify

# Create the application.
APP = flask.Flask(__name__)

with open ('elements.json') as elements_data:
	data = json.load(elements_data)
elements = data['elements']

	#print json.dumps(data, indent=4)

@APP.route('/') #Decorator, decorates APP with function defined. 
def index(): #Defines index function to return "Welcome to..." at url /
	return "Welcome to the world's worst API"

# Returns all elements at url /get_all_elements
@APP.route('/get_all_elements')
def get_all_elements():
	return jsonify(elements)

# Returns element info when atomic no. inputed
@APP.route('/atomic_number/<int:atomic_no>')
def atomic_number(atomic_no):
	for element in elements:
		if element['number'] == atomic_no: 
			return jsonify(element)
	return "No element found!"

# Returns element info when element name inputed
@APP.route('/element_name/<name>')
def element_name(name):
	for element in elements:
		if element['name'].lower() == name.lower(): 
			return jsonify(element)
	return "No element found!"

# Returns elements with atomic numbers over inputed number
@APP.route('/atomic_number/over/<int:atomic_no>')
def atomic_number_over(atomic_no):
	output=[]
	for element in elements:
		if element['number'] > atomic_no: 
			output.append(element)	
	return jsonify(output)

if __name__ == '__main__':
    APP.debug=True
    APP.run(host='0.0.0.0', port='8080')