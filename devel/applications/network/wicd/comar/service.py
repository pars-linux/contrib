serviceType = "local"
serviceDesc = _({
    "en": "Wicd Connection Manager",
    "tr": "Wicd Ağ Yöneticisi"})
serviceConf = "wicd"
serviceDefault = "on"

from comar.service import *

@synchronized
def start():
    loadEnvironment()
    startService(command="/usr/lib/wicd/wicd-daemon.py",
                 pidfile="/var/run/wicd/wicd.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(command="/usr/lib/wicd/wicd-daemon.py")
    stopService(command="/usr/lib/wicd/monitor.py")
    stopService(pidfile="/var/run/wicd/wicd.pid",
                donotify=True)

def status():
    return isServiceRunning("/var/run/wicd/wicd.pid")
