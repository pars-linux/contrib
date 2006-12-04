#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "nessus-core"

def setup():
    shelltools.export("CC", get.CC())
    autotools.configure("--enable-client \
                         --enable-gtk \
                         --enable-syslog")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("/usr/lib/nessus/plugins")
    pisitools.remove("/usr/include/nessus/includes.h")
    pisitools.dodoc("README*", "UPGRADE_README", "CHANGES")
    pisitools.dodoc("doc/*.txt", "doc/ntp/*")
    pisitools.dodir("/var/lib/nessus")
    pisitools.dodir("/var/lib/nessus/logs")
    pisitools.dodir("/var/lib/nessus/users")
