import cv2
cap = cv2.VideoCapture(0)
while True:
    success, imgs = cap.read()
    # img = captureScreen()
   # imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    #img = cv2.cvtColor(imgs, cv2.COLOR_BGR2HSV)
    cv2.imshow('www.diy-nightvision.com', imgs)
    cv2.waitKey(1)