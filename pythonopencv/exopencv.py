import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

#object



thres = 0.45 # Threshold to detect object
nms_threshold = 0.2
#cap = cv2.VideoCapture(0)
# cap.set(3,1280)
# cap.set(4,720)
# cap.set(10,150)

className= []
classFile = 'coco.names'
with open(classFile,'rt') as f:
    className = f.read().rstrip('\n').split('\n')

#print(classNames)
configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)





# face

#from PIL import ImageGrab

path = 'ImagesAttendance'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
     curImg = cv2.imread(f'{path}/{cl}')
     images.append(curImg)
     classNames.append(os.path.splitext(cl)[0])
print(classNames)


def findEncodings(images):
     encodeList = []
     for img in images:
         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
         encode = face_recognition.face_encodings(img)[0]
         encodeList.append(encode)
     return encodeList


def markAttendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name}, "{dtString}')


#### FOR CAPTURING SCREEN RATHER THAN WEBCAM
# def captureScreen(bbox=(300,300,690+300,530+300)):
#     capScr = np.array(ImageGrab.grab(bbox))
#     capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
#     return capScr

encodeListKnown = findEncodings(images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)
count=1


while True:
    success, img = cap.read()

    #object
    classIds, confs, bbox = net.detect(img, confThreshold=thres)
    bbox = list(bbox)
    confs = list(np.array(confs).reshape(1, -1)[0])
    confs = list(map(float, confs))
    # print(type(confs[0]))
    # print(confs)

    indices = cv2.dnn.NMSBoxes(bbox, confs, thres, nms_threshold)
    # print(indices)
    for i in indices:
        i = i[0]
        box = bbox[i]
        x, y, w, h = box[0], box[1], box[2], box[3]
        cv2.rectangle(img, (x, y), (x + w, h + y), color=(0, 255, 0), thickness=2)
        cv2.putText(img, className[classIds[i][0] - 1].upper(), (box[0] + 10, box[1] + 30),
                    cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)




    #facerecog

    # img = captureScreen()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
         matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
         faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
         # print(faceDis)
         matchIndex = np.argmin(faceDis)

         if matches[matchIndex]:
              name = classNames[matchIndex].upper()
               # print(name)
              y1, x2, y2, x1 = faceLoc
              y1, x2, y2, x1 = y1 * 4, x2 * 5, y2 * 5, x1 * 4   #name bar value
             # cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2) #bbox
              cv2.rectangle(img, (x1, y2 -35), (x2, y2), (0, 255, 0), cv2.FILLED)
              cv2.putText(img, name, (x1 + 1, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 0.8, (200,255, 255), 2)
              markAttendance(name)
              cv2.imwrite("image/pepol00" + str(count) + ".jpg", img)
              count+=1


    cv2.imshow('Webcam', img)
    cv2.waitKey(1)