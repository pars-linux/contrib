import os
from comar.service import *

serviceType = "server"
serviceDesc = "Squid Daemon"

def start():
    ret = run("/usr/sbin/squid -DYC")
    if ret == 0:
        notify("System.Service.changed", "started")

def stop():
    ret = run("/usr/sbin/squid -k shutdown")
    if ret == 0:
        notify("System.Service.changed", "stopped")

def reload():
    run("/usr/sbin/squid -k reconfigure")

def status():
    return checkDeamon("/var/run/squid.pid")
