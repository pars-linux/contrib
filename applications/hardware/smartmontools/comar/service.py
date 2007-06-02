from comar.service import *

serviceType="server"
serviceDesc = _({"en": "S.M.A.R.T. monitoring daemon",
                 "tr": "S.M.A.R.T. izleme servisi"})

serviceConf = "smartd.conf"

@synchronized
def start():
    startService(command="/usr/sbin/smartd", pidfile="/var/run/smartd.pid", donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/smartd.pid", donotify=True)

def reload():
    run("/usr/bin/killall -HUP smartd")

def status():
    return isServiceRunning("/var/run/smartd.pid")
