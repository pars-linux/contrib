#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

import os

# package is created from
# http://users.cybercity.dk/%7Edsl145780/z700llpddk-2.0-1.i386.tar.gz
# http://users.cybercity.dk/%7Edsl145780/lexmark-z700-cups-driver-1.1.1-1.i586.tar.gz

WorkDir = get.srcNAME()
NoStrip = "/"

def fixperms(d):
    for root, dirs, files in os.walk(d):
        for name in dirs:
            shelltools.chmod(os.path.join(root, name), 0755)
        for name in files:
            if name.endswith(".h") or name.endswith(".ppd"):
                shelltools.chmod(os.path.join(root, name), 0644)
            elif name.endswith(".a") or name.endswith(".la"):
                shelltools.unlink(os.path.join(root, name))
            else:
                shelltools.chmod(os.path.join(root, name), 0755)

def setup():
    d = "usr/share/cups/model"
    shelltools.makedirs("%s/C" % d)

    for f in shelltools.ls(d):
        if not shelltools.isDirectory("%s/%s" % (d,f)):
            shelltools.move("%s/%s" % (d,f), "%s/C/" % d)

    for f in shelltools.ls("usr/share/cups/model/C/*.ppd.gz"):
        shelltools.system("gunzip -f %s" % f)

    fixperms("usr")

def install():
    pisitools.insinto("/", "usr")

    for f in ["z700core", "printer", "printjob"]:
        t = "liblex%s.so.0" % f
        pisitools.dosym("%s.0.0" % t, "/usr/lib/%s" % t)

    pisitools.removeDir("/usr/include")
    pisitools.removeDir("usr/local/z700cups")

