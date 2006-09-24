import os
from comar.service import *

serviceType = "server"
serviceDesc = "DHCP Daemon"

def start():
    ret = run("start-stop-daemon --start --exec /usr/sbin/dovecot --pidfile /var/run/dovecot/master.pid")
    if ret == 0:
        notify("System.Service.changed", "started")

def stop():
    ret = run("start-stop-daemon --stop --exec /usr/sbin/dovecot --pidfile /var/run/dovecot/master.pid")
    if ret == 0:
        notify("System.Service.changed", "stopped")

def status():
    return checkDeamon("/var/run/dovecot/master.pid")
