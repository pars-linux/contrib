#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Fethi Aymaz <fethi@linux-sevenler.org>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    pass

def build():
    autotools.make("prefix=/usr")

def install():
    autotools.rawInstall("prefix=%s/usr" % get.installDIR())
    pisitools.domove("/usr/man", "/usr/share/man")
    pisitools.dohtml("manual*.html")
    pisitools.dodir("/var/tmp/nxtvdb")
    pisitools.dodoc("CHANGES", "COPYRIGHT", "README*", "TODO")