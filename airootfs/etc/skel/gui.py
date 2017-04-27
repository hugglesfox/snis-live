from tkinter import *
import os


def snislauncher():
    os.system("xterm -e ./snis_launcher")


def sound():
    os.system("pavucontrol")


def internet():
    os.system("xterm -e nmtui")


def shutdown():
    os.system("shutdown")


root = Tk()
label = Label(root, text="System Menu:", bg="white")
label.pack()
snislauncherbutton = Button(root, text="SNIS", command=snislauncher, bg="white")
snislauncherbutton.pack()
soundbutton = Button(root, text="Sound", command=sound, bg="white")
soundbutton.pack()
internetbutton = Button(root, text="Connect to a network", command=internet, bg="white")
internetbutton.pack()
shutdownbutton = Button(root, text="Shutdown PC (in one minute)", command=shutdown, bg="white")
shutdownbutton.pack()
root.configure(background="white")

root.mainloop()
