#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Uğur Çetin <jnmbk@users.sourceforge.net>

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "."

def install():
    shelltools.chmod("freemind.sh", 0755)
    pisitools.insinto("/opt/freemind", "*")
    pisitools.dosym("/opt/freemind/freemind.sh", "/usr/bin/freemind")
    pisitools.remove("/opt/freemind/freemind.bat")
    pisitools.remove("/opt/freemind/Freemind.exe")
    pisitools.remove("/opt/freemind/pisiBuildState")
    #Turkish translation
    shelltools.cd("%s/opt/freemind/lib" % get.installDIR())
    shelltools.system("zip freemind.jar Resources_tr.properties")
    pisitools.remove("/opt/freemind/lib/Resources_tr.properties")