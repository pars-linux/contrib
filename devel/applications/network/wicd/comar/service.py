serviceType = "local"
serviceDesc = _({
    "en": "Wired / Wireless Connection Manager",
    "tr": "Kablolu / Kablosuz Ağ Yöneticisi"})
serviceConf = "wicd"

from comar.service import *

@synchronized
def start():
    loadEnvironment()
    startService(command="/usr/lib/wicd/wicd-daemon.py",
                 pidfile="/var/run/wicd/wicd.pid",
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/wicd/wicd.pid",
                donotify=True)
    stopService(command="/usr/lib/wicd/wicd-daemon.py")
    stopService(command="/usr/lib/wicd/monitor.py")

def status():
    return isServiceRunning("/var/run/wicd/wicd.pid")
