import os
from comar.service import *

serviceType = "server"
serviceDesc = _({"en": "Squid Daemon",
                 "tr": "Squid Sunucusu"})

def start():
    ret = run("/usr/sbin/squid -DYC")
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/usr/sbin/squid -k shutdown")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def reload():
    run("/usr/sbin/squid -k reconfigure")

def status():
    return checkDaemon("/var/run/squid.pid")
