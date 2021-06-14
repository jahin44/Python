from tkinter import*
import tkinter as tk
import cv2
import numpy as np
import webbrowser



#GRAY ONLY
def obj():
    thres = 0.45
    nms_threshold = 0.2
    cap = cv2.VideoCapture(0)

    className = []
    classFile = 'coco.names'
    with open(classFile, 'rt') as f:
        className = f.read().rstrip('\n').split('\n')

    # print(classNames)
    configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
    weightsPath = 'frozen_inference_graph.pb'

    net = cv2.dnn_DetectionModel(weightsPath, configPath)
    net.setInputSize(320, 320)
    net.setInputScale(1.0 / 127.5)
    net.setInputMean((127.5, 127.5, 127.5))
    net.setInputSwapRB(True)

    while True:
        success, img = cap.read()
        classIds, confs, bbox = net.detect(img, confThreshold=thres)
        bbox = list(bbox)
        confs = list(np.array(confs).reshape(1, -1)[0])
        confs = list(map(float, confs))
        # print(type(confs[0]))
        # print(confs)

        indices = cv2.dnn.NMSBoxes(bbox, confs, thres, nms_threshold)

        for i in indices:
            i = i[0]
            box = bbox[i]
            x, y, w, h = box[0], box[1], box[2], box[3]
            cv2.rectangle(img, (x, y), (x + w, h + y), color=(0, 255, 0), thickness=2)
            cv2.putText(img, className[classIds[i][0] - 1].upper(), (box[0] + 10, box[1] + 30),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("Display Object Detection                Q for EXIT", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    cv2.destroyAllWindows()


#GRAY ONLY
def GRAY():
    path = cv2.VideoCapture(0)

    while True:
        success, img = path.read()
        imgc = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        cv2.imshow("Display GRAY                Q for EXIT",imgc)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()









#HUE ONLY
def HLS():
    path = cv2.VideoCapture(0)

    while True:
        success, img = path.read()
        imgHLS = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)

        cv2.imshow("Display HLS           Q for EXIT",imgHLS)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()




#HSV
def HSV():

    path = cv2.VideoCapture(0)

    while True:
        success, img = path.read()
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        cv2.imshow("Display HSV                Q for EXIT", imgHSV)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()




#VIDEO + REC
def Recandvid():
    def empty(a):
          pass

    def stackImages(scale, imgArray):
        rows = len(imgArray)
        cols = len(imgArray[0])
        rowsAvailable = isinstance(imgArray[0], list)
        width = imgArray[0][0].shape[1]
        height = imgArray[0][0].shape[0]
        if rowsAvailable:
            for x in range(0, rows):
                for y in range(0, cols):
                    if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                        imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                    else:
                        imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]),
                                                    None, scale, scale)
                    if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
            imageBlank = np.zeros((height, width, 3), np.uint8)
            hor = [imageBlank] * rows
            hor_con = [imageBlank] * rows
            for x in range(0, rows):
                hor[x] = np.hstack(imgArray[x])
            ver = np.vstack(hor)
        else:
            for x in range(0, rows):
                if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                    imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
                else:
                    imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale,
                                             scale)
                if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
            hor = np.hstack(imgArray)
            ver = hor
        return ver

    path = cv2.VideoCapture(0)
    cv2.namedWindow("TrackBars")
    cv2.resizeWindow("TrackBars", 640, 240)
    cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
    cv2.createTrackbar("Hue Max", "TrackBars", 19, 179, empty)
    cv2.createTrackbar("Sat Min", "TrackBars", 110, 255, empty)
    cv2.createTrackbar("Sat Max", "TrackBars", 240, 255, empty)
    cv2.createTrackbar("Val Min", "TrackBars", 153, 255, empty)
    cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter("Recoded_Vid.avi", fourcc, 20.0, (740, 480))

    while True:
        success, img = path.read()
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
        h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
        s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
        s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
        v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
        v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
        print(h_min, h_max, s_min, s_max, v_min, v_max)
        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])
        mask = cv2.inRange(imgHSV, lower, upper)
        imgResult = cv2.bitwise_and(img, img, mask=mask)

        imgStack = stackImages(0.6, ([img, imgHSV], [mask, imgResult]))
        cv2.imshow("All Display and Recording....       Q for EXIT", imgStack)


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()



def callback(event):
    webbrowser.open_new(event.widget.cget("text"))









root =Tk()
button1= Button(root,text="Video and Record",bg='#47d1d1', command=Recandvid).place(x=40, y=70)
button2= Button(root,text="HSV",bg='#47d1d1',command=HSV).place(x=180, y=70)
button3= Button(root,text="HLS",bg='#47d1d1', command=HLS).place(x=230, y=70)
button4= Button(root,text="GRAY",bg='#47d1d1', command=GRAY).place(x=280, y=70)
button5= Button(root,text="Object Detection",bg='#47d1d1', command=obj).place(x=360, y=70)

lbl = tk.Label(root, text=r"https://github.com/jahin44", fg="blue", cursor="hand2")
lbl.pack()
Label(root, text=" Click here to get more software =>", bg="#eee6ff", fg="black").place(x=0, y=0)

lbl.bind("<Button-1>", callback)
lbl1 = tk.Label(root, text=r"https://jahinhasan.blogspot.com", fg="blue", cursor="hand2")
Label(root, text="     Click here to know about me =>", bg="#eee6ff", fg="black").place(x=0, y=20)

lbl1.pack()
lbl1.bind("<Button-1>", callback)



root.geometry("560x300+120+200")
root.mainloop()