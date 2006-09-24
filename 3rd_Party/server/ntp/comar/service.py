import os
from comar.service import *

serviceType = "server"
serviceDesc = "NTP Daemon"

def start():
    call("System.Service.start", "portmap")
    ret1 = run("/usr/sbin/ntpdate -Q -b -u pool.ntp.org")
    ret2 = run("/usr/sbin/ntpd -p /var/run/ntpd.pid -u ntp:ntp")
    if ret1 == 0 and ret2 == 0:
        notify("System.Service.changed", "started")

def stop():
    ret = run("start-stop-daemon --stop --pidfile /var/run/ntpd.pid --exec /usr/sbin/ntpd")
    if ret == 0:
        notify("System.Service.changed", "stopped")

def status():
    return checkDeamon("/var/run/ntpd.pid")
