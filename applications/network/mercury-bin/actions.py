#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "."
NoStrip = "/"

def setup():
    pass

def build():
    pass

def install():
    pisitools.dosed("startup/startup_linux.sh", "cd \`dirname \$cmdline\`/..", "cd /usr/share/Mercury")
    pisitools.insinto("/usr/share/Mercury/", "*")
    pisitools.insinto("/usr/bin", "startup/startup_linux.sh", "Mercury")
    shelltools.chmod("%s/usr/bin/Mercury" % get.installDIR(), 0755)
    shelltools.system("chmod 644 -R %s/usr/share/Mercury" % get.installDIR())
    
