#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Uğur Çetin <jnmbk@users.sourceforge.net>

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "freemind"

def build():
    shelltools.system("ant dist")

def install():
    shelltools.cd("../bin/dist")
    shelltools.chmod("freemind.sh", 0755)
    pisitools.insinto("/usr/share/freemind", "*")
    pisitools.dosym("/usr/share/freemind/freemind.sh", "/usr/bin/freemind")
    pisitools.remove("/usr/share/freemind/freemind.bat")
    pisitools.remove("/usr/share/freemind/Freemind.exe")