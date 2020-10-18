"""
Author: Rakesh Yadav
Aim: To make a conversational chatbot by using ML, NLTK & tkinter
        through python.
"""

from tkinter import *

appRoot = Tk()

# -- main window ----
appRoot.title("Technobot")
appRoot.geometry("720x552")
appRoot.minsize(400, 300)
appRoot.maxsize(800, 680)


# ------- ***** user-text handling method .i.e, sendBtn()
def sendbtn():
    pass


# -- TOP-frame of appRoot
frame01 = Frame(appRoot, pady=5, bg="pink", borderwidth=2)
frame01.pack(anchor="nw", fill=X)
lable01 = Label(frame01, padx=10, text=" WELCOME to TECHNOBOT ",
                font="Bazooka 12 bold", bg="black", fg="white")
lable01.pack(side=TOP, fill=X)

# -- chatbot-Image Labelling
photo = PhotoImage(file=r'C:\Users\Yadav Ji\Documents\GitHub\TechnoBot\TechnoBot\img\icon chatbot image.png')
photolabel = Label(image=photo, borderwidth=3, bg="#040310", padx=20, pady=100,
                   relief=GROOVE, height=100, width=120).pack(anchor="nw", fill=X)
frameImg = Frame(appRoot, bg="#040319", height=5, borderwidth=2,
                 relief=SUNKEN).pack(side=TOP, fill=X)

# -- bottom-Frame
Frame(appRoot, bg="#040319", height=20, borderwidth=2,
      relief=SUNKEN).pack(side=BOTTOM, fill=X)

# -- Text-Field Framing  ----
frame = Frame(appRoot)
scrollBar = Scrollbar(frame)
msgsTextField = Listbox(frame, width=80, height=20)
scrollBar.pack(side=RIGHT, fill=Y)
msgsTextField.pack(side=LEFT, fill=BOTH, pady=5)
frame.pack()

# ----- User-Entry Field and Send-Button Labeling ---
textField = Entry(appRoot, width=50, borderwidth=5, font="Arial 18 italic"
                  ).pack(side=LEFT, anchor="s")
textBtn = Button(appRoot, text="SEND", width=8, font="Arial 15 bold",
                 textvariable=textField).pack(side=RIGHT, anchor="s")

appRoot.mainloop()
