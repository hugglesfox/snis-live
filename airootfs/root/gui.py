from tkinter import *
import os


def snislauncher():
    os.system("xterm -e cd /space-nerds-in-space && ./snis_launcher")
 

def snisspeech():
    os.system("xterm -e cd /space-nerds-in-space/speech && ./queeg500")
    
    
def sound():
    os.system("pavucontrol")


def internet():
    os.system("xterm -e nmtui")


def shutdown():
    os.system("shutdown now")


root = Tk()
label = Label(root, text="System Menu:", bg="white")
label.pack()
snislauncherbutton = Button(root, text="Space Nerds in Space", command=snislauncher, bg="white")
snislauncherbutton.pack()
speechbutton = Button(root, text="SNIS Speech", command=snisspeech, bg="white")
speechbutton.pack()
soundbutton = Button(root, text="Audio Settings", command=sound, bg="white")
soundbutton.pack()
internetbutton = Button(root, text="Internet Settings", command=internet, bg="white")
internetbutton.pack()
shutdownbutton = Button(root, text="Shutdown PC", command=shutdown, bg="white")
shutdownbutton.pack()
root.configure(background="white")

root.mainloop()
