#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--with-x \
                         --x-includes=/usr/include/X11 \
                         --x-libraries=/usr/lib \
                         --disable-panel-gtk --disable-setup-ui") ##disable unneeded for 
                                                                  ##Pardus desktop

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "BUGS", "NEWS", "README*", "TODO", "THANKS")
