from flask import Flask, jsonify, request
import numpy as np

app = Flask(__name__)

delatts = [{'name' : 'Krishn', 'address' : 'Surat'}]

app.route('/person', method=['GET'])

def details_route():
    return jsonify({'message' : 'Hello'})