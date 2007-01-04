from comar.service import *
import comar
import os

serviceType="server"
serviceDesc = _({"en": "TrouSers",
                 "tr": "TrouSers"})

def unlink():
    try:
        os.unlink("/var/run/tcsd.pid")
    except:
        pass

def load_modul():
    run("/sbin/modprobe tpm")

def start():
    load_modul()
    ret = run("/sbin/start-stop-daemon --start --chuid tss --quiet --background \
                --pidfile /var/run/tcsd.pid --exec /usr/sbin/tcsd")
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop --quiet --pidfile /var/run/tcsd.pid")
    if ret == 0:
        unlink()
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/tcsd.pid")
