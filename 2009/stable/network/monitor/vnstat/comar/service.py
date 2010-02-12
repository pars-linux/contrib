# -*- coding: utf-8 -*-
from comar.service import *

serviceType = "local"
serviceDesc = _({
    "en": "vnStat Daemon",
    "tr": "vnStat Servisi",
})
serviceDefault = "off"

pidFile = "/var/run/vnstat.pid"

@synchronized
def start(boot=False):
    if status():
        return

    startService(command="/usr/sbin/vnstatd", args="--daemon")

@synchronized
def stop():
    stopService(pidfile=pidFile, donotify=True)

def status():
    return isServiceRunning(pidFile)
