from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "VNC sunucusu",
                 "tr": "VNC server"})

@synchronized
def start():
    startService(command="/usr/bin/x11vnc",
                 args="-rfbauth -storepasswd -passwd",
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/bin/x11vnc",
                args="stop",
                donotify=True)

def reload():
    stopService(command="/usr/bin/x11vnc",
                args="reload")

def status():
    return isServiceRunning(command="/usr/bin/x11vnc")
