import socket
import sys
from threading import Thread
import select
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


PORT  = 8050
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

def musicWindow():

    print("\n\t\t\t\tMUSIC window")

    #Client GUI starts here
    window=Tk()

    window.title('Music Window')
    window.geometry("300x300")
    window.configure(bg='lightskyblue')

    selectlabel = label(window,text="select song",bg='lightskyblue',font=("calibri",10))
    selectlabel.place(x=2,y=1)

    listbox=listbox(window,height=10,width=19,activestyle="dotbox",bg="lightskyblue",borderwidth=2,font=("calibri",10))
    listbox.place(x=10,y=10)

    scrollbar1=Scrollbar(listbox)
    scrollbar1.place(relheight=1,relx=1)
    scrollbar1.config(command=listbox.yview)

    playbutton=Button(window,text="play",width=10,bd=1,bg="skyblue",font=("Calibri,10"))
    playbutton.place(x=30,y=200)

    stop=Button(window,text="Stop",bd=1,width=10,bg="skyblue",font=("Calibri",10))
    stop.place(x=200,y=200)

    upload=Button(window,text="Upload",width=10,bd=1,bg="skyblue",font=("Calibri",10))
    upload.place(x=30,y=250)

    dowwnload=Button(window,text-"Download",width=10,bd=1,bg="skyblue",font=("Calibri",10))
    download.place(x=200,y=250)

    infolabel = label(window,text="",fg="blue",font=("Calibri",8))
    infolabel.place(x=4,y=280)

    window.mainloop()

def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    receive_thread = Thread(target=receiveMessage)               #receiving multiple messages
    receive_thread.start()

    musicWindow()

setup()