import os
from comar.service import *

serviceType = "server"
serviceDesc = "Dansguardian Daemon"

def start():
    ret = run("start-stop-daemon --start --quiet --exec /usr/sbin/dansguardian --p /var/run/dansguardian.pid")
    if ret == 0:
        notify("System.Service.changed", "started")

def stop():
    ret = run("start-stop-daemon --stop --quiet --p /var/run/dansguardian.pid")
    if ret == 0:
        notify("System.Service.changed", "stopped")

def reload():
    run("/usr/sbin/dansguardian -g")
    
def status():
    return checkDeamon("/var/run/dansguardian.pid")
