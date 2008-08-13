from comar.service import *

serviceType="server"
serviceDesc = _({"en": "TeamSpeak Server",
                 "tr": "TeamSpeak Sunucusu"})

@synchronized
def start():
    startService(command="/usr/bin/teamspeak-server",
                 args="-db=/var/lib/teamspeak/teamspeak.dbs \
                       -ini=/etc/teamspeak/teamspeak.ini \
                       -sql=/usr/share/teamspeak/sql/ \
                       -log=/var/log/teamspeak/teamspeak.log \
                       -pid=/var/run/teamspeak/teamspeak.pid \
                       -badnames=/etc/teamspeak/bad_names \
                       -httpdocs=/usr/share/teamspeak/http/ \
                       -tcpquerydocs=/usr/share/teamspeak/tcpquerydocs/",
                 detach=True,
                 chuid="teamspeak",
                 makepid=False,
                 donotify=True)

@synchronized
def stop():
    stopService(pidfile="/var/run/teamspeak/teamspeak.pid",
                donotify=True)

    try:
        os.unlink("/var/run/teamspeak/teamspeak.pid")
    except:
        pass

def status():
    return isServiceRunning("/var/run/teamspeak/teamspeak.pid")
