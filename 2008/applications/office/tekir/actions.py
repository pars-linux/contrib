#!/usr/bin/python
# -*- coding: utf-8 -*-

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "tekir-%s-src" % get.srcVERSION()

def install():
    pisitools.export("JAVA_HOME", "/opt/sun-jdk")
    pisitools.dosed("resources/tekir-prod-ds.xml",
                    "<connection-url>jdbc:hsqldb:.</connection-url>",
                    "<connection-url>jdbc:hsqldb:file:/var/db/tekir/tekirDB</connection-url>")

    pisitools.dosed('build.xml',
                    '<property name="profile" value="dev" />',
                    '<property name="profile" value="prod" />')

    pisitools.dosed('resources/META-INF/application.xml',
                    '<context-root>/</context-root>',
                    '<context-root>/tekir</context-root>')

    shelltools.system("ant clean explode -Djboss.home=%s/opt/jboss4" % get.installDIR())
    pisitools.insinto("/var/db/tekir", "database/hsqldb/tekirDB.properties")
    pisitools.insinto("/usr/share/tekir", "database/hsqldb/tekirDB.log")
