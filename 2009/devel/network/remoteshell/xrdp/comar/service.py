from comar.service import *

serviceType="server"
serviceDesc = _({"en": "Xrdp remote desktop server",
                 "tr": "Xrdp uzak masaustu sunucusu"})

@synchronized
def start():
    startService(command="/usr/sbin/xrdp",
                 pidfile="/var/run/xrdp.pid",
                 donotify=True)
    startService(command="/usr/sbin/xrdp-sesman",
                 pidfile="/var/run/xrdp.pid",
                 donotify=True)

@synchronized
def stop():  
    stopService(command="/usr/sbin/xrdp-sesman",
                args="--kill",
                donotify=True)
    stopService(command="/usr/sbin/xrdp",
                args="--kill",
                donotify=True)

def status():
    return isServiceRunning("/var/run/xrdp.pid")
