"""
Author: Rakesh Yadav
Aim: To make a conversational chatbot by using ML, NLTK & tkinter
        through python.
"""

from tkinter import *

from TechnoBot.src.technobot import chatbot

appRoot = Tk()
icon_photo = PhotoImage(file='../img/chatbot icon.png')

# Setting icon of master window
appRoot.iconphoto(False, icon_photo)
# -- main window ----
appRoot.title("Technobot")
appRoot.geometry("720x552")
appRoot.minsize(400, 300)
appRoot.maxsize(800, 680)


# ------- ***** user-text handling function .i.e, sendBtn()
def sendbtn():
    user_query = textField.get()
    response_of_bot = chatbot.get_response(user_query)
    msgsTextField.insert(END, "YOU          :   " + user_query)
    msgsTextField.insert(END, "TECHNOBOT    :   " + str(response_of_bot))
    textField.delete(0, END)
    msgsTextField.yview(END)


# ----- *** auto-invoking function by Pressing 'ENTER KEY'
def auto_invoke_enter(event):
    textBtn.invoke()


# --- method to binding main window (i.e., appRoot ) with 'ENTER KEY'
appRoot.bind('<Return>', auto_invoke_enter)

# -- TOP-frame of appRoot
frame01 = Frame(appRoot, pady=5, bg="#800000", borderwidth=3)
frame01.pack(anchor="nw", fill=X)
label01 = Label(frame01, padx=10, text=" TECHNOBOT  ",
                font="ALGERIAN 14 bold", bg="#800080", fg="white")
label01.pack(side=TOP, fill=X)

# -- chatbot-Image Labelling
photo = PhotoImage(file='../img/icon.png')
photolabel = Label(image=photo, borderwidth=3, bg="#040310", padx=20, pady=100,
                   relief=GROOVE, height=100, width=120).pack(anchor="nw", fill=X)
frameImg = Frame(appRoot, bg="#040319", height=5, borderwidth=2,
                 relief=SUNKEN).pack(side=TOP, fill=X)

# ----- bottom-Frame   --------
Frame(appRoot, bg="#040319", height=20, borderwidth=2,
      relief=RAISED).pack(side=BOTTOM, fill=X)

# ---- Text-Field Framing  ----
frame = Frame(appRoot, bg="#0000A0")
scrollBar = Scrollbar(frame, background="#808080")
msgsTextField = Listbox(frame, width=98, height=20, bg="#808080", yscrollcommand=scrollBar.set)
scrollBar.pack(side=RIGHT, fill=Y)
msgsTextField.pack(side=LEFT, fill=BOTH, pady=3)
frame.pack()

# ----- User-Entry Field and Send-Button Labeling -----------
textField = Entry(appRoot, width=40, borderwidth=4, font="Verdana 18 ", bg="#D7DADA")
textField.pack(side=LEFT, anchor="s")
textBtn = Button(appRoot, text="Ask Me", width=8, font="Georgia 12", bg="#000000", fg="white",
                 command=sendbtn)
textBtn.pack(side=RIGHT, anchor="s")

appRoot.mainloop()