import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import requests
import urllib
import csv
from datetime import date
import serial

# ESP32-CAM IP address
esp32cam_url = 'http://10.100.8.24/640x480.jpg'
arduino = serial.Serial('/dev/cu.usbmodem1401', 9600)

rollNo={'MUSKAN':'2021UCA1814'}

# Function to fetch images from ESP32-CAM
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
    # encodeList = []
    # i = 0
    # for img in images:
    #     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #     encode = face_recognition.face_encodings(img)[0]
    #     encodeList.append(encode)
    #     print(f'Encoding {i}/{len(mylist)} done!')
    #     i=i+1
    # return encodeList


def markAttendance(name):
    with open('./Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{rollNo[name]},{dtString}')
    f.close()


encodelistknown = find_encodings(images)
print('Encoding Complete!')

file=open('./Attendance.csv','a')
file.writelines(f'{"ATTENDANCE for - "},{date.today()}')
file.writelines(f'\n{"NAME"},{"ROLL NUMBER"},{"TIMESTAMP"}')
file.close()

directions = {
    1: "Left Back",
    2: "Backward",
    3: "Backward Right",
    4: "Left",
    5: "Stay Still",
    6: "Right",
    7: "Forward Left",
    8: "Forward",
    9: "Forward Right"
}

# Function to send direction to Arduino via serial port
def send_direction(direction):
    print("Direction:", directions[direction])
    arduino.write(bytes([direction]))

# Function to compute direction based on the detected face
def compute_direction(bound, init_area=40000):
    center = (320, 240)
    curr = (bound[0] + bound[2] / 2, bound[1] + bound[3] / 2)
    out = 5  # Stay still by default

    if bound[2] * bound[3] > init_area + 5000 or bound[1] < 50:
        out = 2  # Move backward if object is approaching or too close
    elif bound[2] * bound[3] < init_area - 5000 or (bound[1] + bound[3]) > 430:
        out = 8  # Move forward if object is moving away or too far
    elif curr[0] > center[0] + 100:
        out = 6  # Move right if object is to the right of the center
    elif curr[0] < center[0] - 100:
        out = 4  # Move left if object is to the left of the center
    elif curr[1] < center[1] - 50:
        out = 7  # Move forward-left if object is above the center
    elif curr[1] > center[1] + 50:
        out = 9  # Move forward-right if object is below the center

    return out

cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function to detect and display Muskan's face from ESP32-CAM
def detect_and_display_esp32cam(frame):
    imgS = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    faceCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodelistknown, encodeFace)
        faceDis = face_recognition.face_distance(encodelistknown, encodeFace)
        print(faceDis)
        matchIndex = np.argmin(faceDis)
        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            if name == "MUSKAN":
                direction = compute_direction((x1, y1, x2 - x1, y2 - y1))
                send_direction(direction)

    cv2.imshow('ESP32-CAM', frame)

try:
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise IOError("Failed to open camera")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to retrieve frame")
            break

        detect_and_display_esp32cam(frame)

        if cv2.waitKey(1) == 27:  # ESC key
            break

except Exception as e:
    print("Error:", e)




while True:
    # Capture an image from ESP32-CAM
    img = get_esp32cam_image()

    if img is not None:
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        faceCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

        for encodeFace, faceLoc in zip(encodesCurFrame, faceCurFrame):
            matches = face_recognition.compare_faces(encodelistknown, encodeFace)
            faceDis = face_recognition.face_distance(encodelistknown, encodeFace)
            print(faceDis)
            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                detect_and_display_esp32cam(frame)



        cv2.imshow('ESP32-CAM', img)
        cv2.waitKey(1)

