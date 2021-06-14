import cv2
import os
import time

path = "image"
cambright= 190
modulevalu = 100
minblur= 10
grayimg= False
saveimg = True
showimg=True
imgwidth= 600
imghight=500

global countfolder
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,cambright)

count= 0
countsave=0
def saveDatafun():                         #create new file image0
    global countfolder
    countfolder=0
    while os.path.exists(path+str(countfolder)):
        countfolder = countfolder+1
    os.makedirs(path+str(countfolder))
if saveimg:saveDatafun()

while True:
    suss,img =cap.read()
    img=cv2.resize(img,(imgwidth,imghight))
    if grayimg:img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    if saveimg:
        blur= cv2.Laplacian(img,cv2.CV_64F).var()
        if count % modulevalu  ==0 and blur > minblur:
            nowTime=time.time()                           #real time save img in new name 
            cv2.imwrite(path+str(countfolder)+'/'+str(countsave)+" " + str(int(blur))+" "+str(nowTime)+".jpg",img)
            countsave+=1

    if showimg:
        cv2.imshow("image",img)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break


cap.release()
cv2.destroyWindow()

