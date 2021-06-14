import cv2
import numpy as np
import face_recognition
import os
import time
from datetime import datetime

# from PIL import ImageGrab
countsave=0
path = (r"C:\Users\PC\Desktop\find mask\p")
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
     curImg = cv2.imread(f'{path}/{cl}')
     images.append(curImg)
     classNames.append(os.path.splitext(cl)[0])
     nowTime = time.time()  # real time save img in new name
     cv2.imwrite(path+ '/' " " + str() + " %H" + str(nowTime) + ".jpg", curImg)
     countsave += 1
print(classNames)
