from tkinter import Tk, Label, Button
import os


def snislauncher():
    os.system("xterm -e 'cd /space-nerds-in-space && ./snis_launcher'")

def snisspeech():
    os.system("xterm -e 'cd /space-nerds-in-space/speech && ./queeg500'")

def wireless():
    os.system("echo 'interface = ' $(ls -1 /sys/class/net | grep '\<w.*\>') | head -1) >> /etc/hostapd/hostapd.conf")
    os.system("systemctl start dnsmasq.service && systemctl start hostapd.service")

def dhcp():
    os.system("systemctl start dnsmasq.service")

def sound():
    os.system("pavucontrol")

def internet():
    os.system("xterm -e 'wifi-menu -o'")

def shutdown():
    os.system("systemctl poweroff")

root = Tk()
label = Label(root, text="System Menu:", bg="white")
label.pack()
snislauncherbutton = Button(root, text="Start Space Nerds in Space", command=snislauncher, bg="white")
snislauncherbutton.pack()
speechbutton = Button(root, text="SNIS Speech", command=snisspeech, bg="white")
speechbutton.pack()
soundbutton = Button(root, text="Audio Settings", command=sound, bg="white")
soundbutton.pack()
internetbutton = Button(root, text="Setup Wifi", command=internet, bg="white")
internetbutton.pack()
createapbutton = Button(root, text="Create Wireless Access Point", command=wireless, bg="white")
createapbutton.pack()
startdhcp = Button(root, text="Start DHCP Server on Ethernet", command=dhcp, bg="white")
startdhcp.pack()
shutdownbutton = Button(root, text="Shutdown PC", command=shutdown, bg="white")
shutdownbutton.pack()
root.configure(background="white")

root.mainloop()
