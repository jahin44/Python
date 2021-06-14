from tkinter import *
root=Tk()
import cv2

root.geometry("600x400+120+120")

#frame=Frame(root,width=500,height=200)

def rightClick(event):
    print("right clicked")
    callme()
def leftClick (event):
    print("left clicked")
    callme1()
def middleClick(event):
    print("middle clicked")
    callme()
    callme1()


def callme1():
    ja = cv2.imread("image/joy.jpg")
    # ja1=cv2.imread("image/circlers.jpg")

    # add1 = cv2.addWeighted(ja,0.5,ja1,0.5,2)
    # gray= cv2.cvtColor(add1,cv2.COLOR_BGR2HSV)

    # img= cv2.resize(ja,(600,500))
    # img= cv2.resize(ja,(0,0),fy=0.50,fx=.40)

    # img1=cv2.imwrite("image/circlers.jpg",img)
    img = ja[0:900, 0:900]
    # img=cv2.GaussianBlur(img,(9,9),0)
    # img=cv2.medianBlur(img,1)
    cv2.imshow("image", img)

    if cv2.waitKey() & 0xFF == 27:
        cv2.destroyWindow(0)


def callme():
    ja = cv2.imread("image/circle.jpg")
    # ja1=cv2.imread("image/circlers.jpg")

    # add1 = cv2.addWeighted(ja,0.5,ja1,0.5,2)
    # gray= cv2.cvtColor(add1,cv2.COLOR_BGR2HSV)

    # img= cv2.resize(ja,(600,500))
    # img= cv2.resize(ja,(0,0),fy=0.50,fx=.40)

    # img1=cv2.imwrite("image/circlers.jpg",img)
    img = ja[0:900, 0:900]
    # img=cv2.GaussianBlur(img,(9,9),0)
    # img=cv2.medianBlur(img,1)
    cv2.imshow("image", img)

    if cv2.waitKey() & 0xFF == 27:
        cv2.destroyWindow(0)

#UserName=Label(root,text="Name")
#password =Label(root,text="password")

button =Button(root,text="fun",command=callme)
button.place(x=10,y=10)

#frame = Frame(root, width=300, heigt =400)
button.bind("<Button-1>",rightClick)
button.bind("<Button-2>",middleClick)
button.bind("<Button-3>",leftClick)

# entry1=Entry(root)
#entry2=Entry(root)
#UserName.grid(row=0,sticky=E)
#entry1.grid(row=0,column=1)

#password.grid(row=1,column=0)
#entry2.grid(row=1,column=1)

C=Checkbutton(root,text="keep me logged in ")
C.place(x=30,y=40)

#button.pack()
#UserName.pack(fill=X)
#password.pack(side =LEFT,fill=Y)

root.mainloop()

