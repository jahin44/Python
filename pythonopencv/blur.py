import cv2
img = cv2.imread("image/baby.jpg")
blur_image = cv2.GaussianBlur(img, (7,7), 0)
cv2.imshow('Original image',img)
cv2.imshow('Blur image',blur_image)
cv2.waitKey(0)