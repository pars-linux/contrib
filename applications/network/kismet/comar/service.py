serviceType = "local"
serviceDesc = _({"en": "KISMET Server",
                 "tr": "KISMET Sunucusu"})

from comar.service import *

def check_config():
    if not os.path.exists("/etc/kismet.conf"):
        fail("Configuration file /etc/kismet.conf not found")

def start():
    check_config()

    ret = run("/sbin/start-stop-daemon --start --quiet --pidfile /var/run/kismet_server.pid \
               --background --make-pidfile --exec /usr/bin/kismet_server \
               -- %s" % config.get("KISMET_SERVER_OPTIONS", ""))
    if ret == 0:
        notify("System.Service.changed", "started")
    else:
        fail("Unable to start service")

def stop():
    ret = run("/sbin/start-stop-daemon --stop --quiet --pidfile /var/run/kismet_server.pid")
    if ret == 0:
        notify("System.Service.changed", "stopped")
    else:
        fail("Unable to stop service")

def status():
    return checkDaemon("/var/run/kismet_server.pid")
