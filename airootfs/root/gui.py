from tkinter import Tk, Label, Button, Toplevel
import os

def popup(text):
    toplevel = Toplevel()
    toplevel.configure(background="black")
    toplevel.title("Notice")

    l = Label(toplevel, text=str(text), font=("Lucida Console", 16), fg="lime green", bg="black")
    l.pack()

    b = Button(toplevel, text="Close", command=toplevel.destroy, font=("Lucida Console", 12), fg="lime green", bg="black")
    b.pack()
    
    toplevel.mainloop()

def dhcp(interface):
    os.system("ip addr add 10.0.0.1/24 dev " + str(interface))
    os.system("systemctl restart dnsmasq.service")

def snislauncher():
    os.system("xterm -e 'cd /space-nerds-in-space && ./snis_launcher'")

def snisspeech():
    os.system("xterm -e 'cd /space-nerds-in-space/speech && ./queeg500'")

def hotspot():
    os.system("echo 'interface='$(ls -1 /sys/class/net | grep '\<w.*\>' | head -1) >> /etc/hostapd/hostapd.conf")
    dhcp("$(ls -1 /sys/class/net | grep '\<w.*\>' | head -1)")
    dhcp("$(ls -1 /sys/class/net | grep '\<e.*\>' | head -1)")
    os.system("systemctl start hostapd.service")
    os.system("xterm -e 'echo \"Started dnsmaq on ethernet interface $(ls -1 /sys/class/net | grep '\<e.*\>' | head -1) and wireless interface $(ls -1 /sys/class/net | grep '\<w.*\>' | head -1)  \" && read  -n 1 -p \"Press any key to continue..\"'")
    popup("Created a Router ")
    
def sound():
    os.system("pavucontrol")

def internet():
    os.system("xterm -e 'wifi-menu -o'")

def shutdown():
    os.system("systemctl poweroff")

root = Tk()
root.title("Menu")
root.configure(background="black")

label = Label(root, text="System Menu", font=("Lucida Console", 20), fg="lime green", bg="black")
label.pack()

snislauncherbutton = Button(root, text="Start Space Nerds in Space", command=snislauncher, font=("Lucida Console", 12), fg="lime green", bg="black")
snislauncherbutton.pack()

speechbutton = Button(root, text="SNIS Speech", command=snisspeech, font=("Lucida Console", 12), fg="lime green", bg="black")
speechbutton.pack()

soundbutton = Button(root, text="Audio Settings", command=sound, font=("Lucida Console", 12), fg="lime green", bg="black")
soundbutton.pack()

internetbutton = Button(root, text="Setup Wifi", command=internet, font=("Lucida Console", 12), fg="lime green", bg="black")
internetbutton.pack()

createapbutton = Button(root, text="Setup 'Router' (wireless (if applicable) and ethernet)", command=hotspot, font=("Lucida Console", 12), fg="lime green", bg="black")
createapbutton.pack()

shutdownbutton = Button(root, text="Shutdown PC", command=shutdown, font=("Lucida Console", 12), fg="lime green", bg="black")
shutdownbutton.pack()

root.mainloop()
