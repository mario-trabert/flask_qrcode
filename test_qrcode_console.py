from __future__ import print_function
#import pyzbar.pyzbar as pyzbar
#import zbar as pyzbar
from pyzbar import pyzbar
import numpy as np
import cv2
import requests

def decode(im):
    # Find barcodes and QR codes
    decodedObjects = pyzbar.decode(im)
    print("gehe in decode()")
    # Print results
    for obj in decodedObjects:
        print('Type : ', obj.type)
        print('Data : ', obj.data, '\n')

    return decodedObjects

# Main
if __name__ == '__main__':
    # Read image
    cam = cv2.VideoCapture(0)

    ret_val, img = cam.read()
    decodedObjects = decode(img)
