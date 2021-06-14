import pyautogui
import time
from tkinter import*

sp=1
def click_me():

    sl=enter.get()
    sp=enter1.get()
    if sl =="":
        print("Text and number")
    else:
             ru = sp
             mass = sl
             time.sleep(2)
             count = 0
             while (count < int(ru)):
                count = count + 1
                time.sleep(.5)
                pyautogui.typewrite(mass)
                pyautogui.press('enter')



root =Tk()


S = StringVar()
enter= Entry(root).place(x=150, y=0)
enter1= Entry(root).place(x=150, y=21)
#enter.pack()
#enter1.pack()

Tk.root(root, text="First Name").grid(row=0)
Tk.root(root, text="Last Name").grid(row=1)

e1 = Tk.Entry(root)
e2 = Tk.Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)



button= Button(root,text="send", command=click_me).place(x=200, y=40)
#button.pack()
Label(root, text="Messages", bg="#FFFF00", fg="black").place(x=80, y=0)
Label(root, text=" Number ", bg="#FFFF00", fg="black").place(x=80, y=20)
Label(root, text=" Hey there, this is message bombing software.\n"
                 " First of all type message then type the number how many time you want to send\n "
                 "this message then click in send button and within 2 second go to the text bar in your PC ", bg="#eee6ff", fg="black").place(x=0, y=70)


root.geometry("480x300+120+200")
root.mainloop()


