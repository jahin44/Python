import cv2
ja=cv2.imread("image/circle.jpg")
#ja1=cv2.imread("image/circlers.jpg")

#add1 = cv2.addWeighted(ja,0.5,ja1,0.5,2)
#gray= cv2.cvtColor(add1,cv2.COLOR_BGR2HSV)

#img= cv2.resize(ja,(600,500))
#img= cv2.resize(ja,(0,0),fy=0.50,fx=.40)

#img1=cv2.imwrite("image/circlers.jpg",img)
img= ja[0:900,0:900]
#img=cv2.GaussianBlur(img,(9,9),0)
#img=cv2.medianBlur(img,1)
cv2.imshow("image",img)

if cv2.waitKey() & 0xFF == 27:
    cv2.destroyWindow(0)
