import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import time
import requests
import urllib
import csv
from datetime import date
import serial


esp32cam_url = 'http://10.100.8.24/640x480.jpg'
arduino = serial.Serial('/dev/cu.usbmodem1401', 9600)
time.sleep(2)  # Wait for initialization
print("Initialized")

path = '/Users/pulkitbatra/Downloads/FaceRecognitionCar/ImagesBasic'
images = []
classNames = []
mylist = os.listdir(path)
print(mylist)
for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def get_esp32cam_image():
    try:
        response = requests.get(esp32cam_url, timeout=10)
        if response.status_code == 200:
            img_array = np.array(bytearray(response.content), dtype=np.uint8)
            img = cv2.imdecode(img_array, -1)
            return img
    except Exception as e:
        print(f"Error fetching image from ESP32-CAM: {str(e)}")
    return None


path = '/Users/pulkitbatra/Downloads/FaceRecognitionCar/ImagesBasic'
images = []
classNames = []
mylist = os.listdir(path)
print(mylist)
for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)




def find_encodings(images):
    encodeList = []
    i = 0
    for img in images:
        # Check if the image is empty
        if img is None:
            print(f"Failed to read image {i + 1}/{len(images)}")
            continue
        
        # Convert the image to RGB format
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        
        # Find face encodings in the image
        face_encodings = face_recognition.face_encodings(img)
        
        # Check if any face encodings are found
        if len(face_encodings) > 0:
            encode = face_encodings[0]  # Take the first face encoding
            encodeList.append(encode)
        else:
            print(f"No face found in image {i + 1}/{len(images)}")
        
        # Print progress
        print(f'Encoding {i + 1}/{len(images)} done!')
        i += 1
    return encodeList
