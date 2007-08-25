from comar.service import *
import signal

serviceType = "server"
serviceDesc = _({"en": "TCP redirector",
                 "tr": "TCP yönlendirici"})
serviceDefault = "off"

@synchronized
def start():
    startService(command="/usr/sbin/rinetd",
                 args="-c /etc/rinetd.conf",
                 pidfile= "/var/run/rinetd.pid",
                 donotify=True)
@synchronized
def stop():
    stopService(command="/usr/sbin/rinetd",
                donotify=True)

def status():
    return isServiceRunning("/var/run/rinetd.pid")

def reload():
    stopService(command="/usr/sbin/rinetd",
                args="reload")