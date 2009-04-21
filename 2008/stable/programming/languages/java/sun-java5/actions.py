#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006,2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."
NoStrip = "/"
Name = "5.0u16"

def setup():
    shelltools.system("chmod +x construct.sh")
    shelltools.system("sh jdk-%s-dlj-linux-i586.bin --accept-license" % Name)

def install():
    pisitools.dodir("/opt")
    shelltools.system("./construct.sh . %s/opt/sun-java5-jdk %s/opt/sun-java5-jre"% (get.installDIR(),get.installDIR()))

    for doc in ["COPYRIGHT", "LICENSE", "README.html", "THIRDPARTYLICENSEREADME.txt"]:
        doc_file = "%s/opt/sun-java5-jdk/%s" % (get.installDIR(),doc)
        pisitools.dodoc(doc_file)
        shelltools.unlink(doc_file)
