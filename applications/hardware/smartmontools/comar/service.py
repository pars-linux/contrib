from comar.service import *
import comar
import os

serviceType="server"
serviceDesc = _({"en": "S.M.A.R.T. monitoring daemon",
                 "tr": "S.M.A.R.T. monitoring daemon"})

serviceConf = "smartd.conf"

def unlink():
    try:
        os.unlink("/var/run/smartd.pid")
    except:
        pass

def start():

    ret = run("/sbin/start-stop-daemon --start --exec /usr/sbin/smartd --pidfile /var/run/smartd.pid  -- -p /var/run/smartd.pid")

    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon  --stop --exec /usr/sbin/smartd --pidfile /var/run/smartd.pid")

    if ret == 0:
        unlink()
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")
