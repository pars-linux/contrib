#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

serviceType = "server"
serviceDesc = _({"en": "JBoss J2EE Application Server",
                 "tr": "JBoss J2EE Uygulama Sunucusu"})

from comar.service import *

@synchronized
def start():
    loadEnvironment()
    if not os.environ.has_key("JAVA_HOME"):
        fail("JAVA_HOME is not set")
    javapath = os.environ["JAVA_HOME"]

    os.chdir("/opt/jboss4")

    startService(command="%s/bin/java" % javapath,
                 args="-Dprogram.name=run.sh -server -Xms128m -Xmx512m -Dsun.rmi.dgc.client.gcInterval=3600000 -Dsun.rmi.dgc.server.gcInterval=3600000 -Djava.net.preferIPv4Stack=true -Djava.endorsed.dirs=/opt/jboss4/lib/endorsed -classpath /opt/jboss4/bin/run.jar:/opt/sun-jdk/lib/tools.jar org.jboss.Main",
                 pidfile="/var/run/jboss4.pid",
                 detach=True,
                 makepid=True,
                 donotify=True)

@synchronized
def stop():
    loadEnvironment()
    if not os.environ.has_key("JAVA_HOME"):
        fail("JAVA_HOME is not set")
    javapath = os.environ["JAVA_HOME"]

    # Set JBoss Home and Classpath
    JBOSS_HOME = "/opt/jboss4"
    JBOSS_CLASSPATH = "%s/bin/shutdown.jar:%s/client/jbossall-client.jar" % (JBOSS_HOME,JBOSS_HOME)

    os.chdir(JBOSS_HOME)

    stopService(command="%s/bin/java" % javapath,
                args="-classpath %s org.jboss.Shutdown -S" % JBOSS_CLASSPATH,
                donotify=True)

def status():
    return isServiceRunning("/var/run/jboss4.pid")
