import os
from comar.service import *

serviceType = "server"
serviceDesc = "BIND Daemon"

def start():
    ret = run("start-stop-daemon --start --quiet --exec /usr/sbin/named --p /var/run/named/named.pid -u named -n 1")
    if ret == 0:
        notify("System.Service.changed", "started")

def stop():
    ret = run("start-stop-daemon --stop --quiet /var/run/named/named.pid --exec /usr/sbin/named -- stop")
    if ret == 0:
        notify("System.Service.changed", "stopped")

def status():
    return checkDeamon("/var/run/named/named.pid")
