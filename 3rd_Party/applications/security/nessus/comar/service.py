import os
from comar.service import *

serviceType = "local"
serviceDesc = "Nessus Daemon"

def start():
    ret = run("start-stop-daemon --start --quiet --exec /usr/sbin/nessusd -- -D --quiet")
    if ret == 0:
        notify("System.Service.changed", "started")

def stop():
    ret = run("start-stop-daemon --stop --quiet --exec /usr/sbin/nessusd")
    if ret == 0:
        notify("System.Service.changed", "stopped")
