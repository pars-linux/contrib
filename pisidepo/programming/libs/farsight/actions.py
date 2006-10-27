#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("./autogen.sh")
    autotools.configure("--disable-gtk-doc \
                                            --disable-sequence-diagrams \
                                            --disable-msnwebcam \
                                            --disable--msnavconf \
                                            --disable-yahoowebcam \
                                            --enable-rtp \
                                            --enable-sofia-sip \
                                            --enable-jingle-p2p")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("ChangeLog", "AUTHORS", "README", "TODO")