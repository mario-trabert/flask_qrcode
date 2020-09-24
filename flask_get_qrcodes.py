from flask import Flask, jsonify, session
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import requests
#from flask.ext.session import Session


app = Flask(__name__)
#sess = Session()

def decode():
    # init cam
    cam = cv2.VideoCapture(0)
    ret_val, img = cam.read()

    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(img)
    dict_qrcodes = {}
    counter = 0
    # Print results
    for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data, '\n')
        
        dict_qrcodes[counter] = obj.data
        counter += 1

    return dict_qrcodes

@app.route('/test')
def get_current_user():
    dict_test = {}
    dict_test[1] = "medi01"
    dict_test[2] = "medi02"
    #return jsonify(username="Test", passd="test")
    return jsonify(dict_test)

@app.route('/get_qrcodes')
def get_qrcodes():
    response = jsonify(decode())
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['content-type'] = 'application/json'
    return(response)

#start the web server at localhost on port 1337
if __name__ == '__main__':
    #app.secret_key = 'super secret key'
    #app.config['SESSION_TYPE'] = 'filesystem'
    #sess.init_app(app)
    app.run(host='0.0.0.0', port=1337, debug=True)
   