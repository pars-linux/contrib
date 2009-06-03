from comar.service import *
import comar
import os

serviceType="server"
serviceDesc = _({"en": "WebCleaner",
                 "tr": "WebCleaner"})



def unlink():
    try:
        os.unlink("/var/run/webcleaner.pid")
    except:
        pass

def start():
    ret = run("/sbin/start-stop-daemon --start --quiet --background \
                --make-pidfile --pidfile /var/run/webcleaner.pid --exec /usr/bin/webcleaner")
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop --quiet --pidfile=/var/run/webcleaner.pid")
    if ret == 0:
        unlink()
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/webcleaner.pid")