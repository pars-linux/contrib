#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

datadir = "/usr/share/planeshift"

def setup():
    shelltools.system("./autogen.sh")

    autotools.configure("--disable-debug \
                         --enable-optimize-mode-debug-info=no \
                         --with-optimize-debug-info=no \
                         --enable-separate-debug-info=no \
                         --enable-cpu-specific-optimizations=no \
                         --with-cs-prefix=/usr \
                         --with-cel-prefix=/usr \
                         --with-x \
                         --with-cal3d \
                         --with-bfd")

def build():
    pisitools.dosed("Jamconfig", "-O3", get.CXXFLAGS())

    # Let's only build client for now.
    shelltools.system("jam -aq client")

def install():
    shelltools.system("jam -s DESTDIR=%s install_bin" % get.installDIR())

    for data in ["data/eedit", "data/npcbehave.xml", "data/npcdefs.xml", "data/pvp_regions.xml"]:
        pisitools.insinto("%s/data" % datadir, data)

    for f in ["lang", "*.cfg"]:
        pisitools.insinto(datadir, f)

    pisitools.dosym("/usr/share/fonts/dejavu/DejaVuSerif.ttf", "%s/data/ttf/arial.ttf" % datadir)

    pisitools.domove("/usr/bin/*", datadir)
    pisitools.removeDir("/usr/bin")

    pisitools.dodoc("docs/*.txt")
    pisitools.dohtml("docs/*.html")
