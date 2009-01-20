from comar.service import *

serviceType = "local"
serviceDesc = _({"en": "Last.fm Submission Daemon",
                 "tr": "Last.fm Bildirim Sunucusu"})
serviceDefault = "off"

pidfile = "/var/run/scrobby/scrobby.pid"

@synchronized
def start():
    startDependencies("mpd")
    startService(command="/usr/bin/scrobby",
                 pidfile=pidfile,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile=pidfile,
                donotify=True)

def status():
    return isServiceRunning(pidfile)
