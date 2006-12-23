serviceType = "server"
serviceDesc = _({"en": "BIND Daemon",
                 "tr": "BIND DNS Sunucusu"})
serviceConf = "named"

import os
from comar.service import *

def start():
    ret = run("/sbin/start-stop-daemon --start --quiet --exec /usr/sbin/named --p /var/run/named/named.pid -u named -n \
              -- %s %s" % (config.get("OPTION", ""), config.get("CPU", "")))
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop --quiet /var/run/named/named.pid --exec /usr/sbin/named -- stop")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDeamon("/var/run/named/named.pid")
