#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("other/SimpleServer/simpleserver.in", "@_simiasdatadir_@", "/var/lib/simias")
    
    pisitools.dosed("other/SimpleServer/SimpleDomain.cs", \
        "private string serverDocumentPath = \"../../etc/SimpleServer.xml\";",
        "private string serverDocumentPath = \"/etc/SimpleServer.xml\";")

    autotools.configure("--with-simiasdatadir=/var/lib/simias")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    shelltools.cd("other/SimpleServer")
    autotools.rawInstall("DESTDIR=%s install-simpleserver" % get.installDIR())
    pisitools.dodir("/var/lib/simias")
