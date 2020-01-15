from __future__ import print_function
#import pyzbar.pyzbar as pyzbar
from pyzbar import pyzbar

import numpy as np
import cv2
import requests

state_old = "undetected"
state_new = "undetected"
'''
    Start
    -> undetected
    
    User shows QR-code
    -> detected
        -> send_request_to_server
        
    User removes QR-code
    -> undetected
    
    
'''


def decode(im):
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(im)

    # Print results
    for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data, '\n')

    return decodedObjects


# Display barcode and QR code location
def display(im, decodedObjects):

    # Loop over all decoded objects
    for decodedObject in decodedObjects:
        state_new = "detected"
        points = decodedObject.polygon

        # If the points do not form a quad, find convex hull
        if len(points) > 4:
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            hull = list(map(tuple, np.squeeze(hull)))
        else:
            hull = points;

        # Number of points in the convex hull
        n = len(hull)

        # Draw the convext hull
        for j in range(0, n):
            cv2.line(im, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)

        #if state_new == "detected" and state_old == "undetected":
            #send_request()

        state_old = state_new
    # Display results
    cv2.imshow("Results", im);


def send_request(data):
    URL = "http://127.0.0.1:3000/json"
    PARAMS = {'data': data}
    r = requests.get(url=URL, params=PARAMS)

    # extracting data-response in json format
    data = r.json()

# Main
if __name__ == '__main__':

    # Read image
    cam = cv2.VideoCapture(0)
    # im = cv2.imread('zbar-test.jpg')

    while True:
        ret_val, img = cam.read()
        #cv2.imshow('my webcam', img)
        if cv2.waitKey(1) == 27:
            break  # esc to quit
        decodedObjects = decode(img)
        display(img, decodedObjects)

    cv2.destroyAllWindows()


