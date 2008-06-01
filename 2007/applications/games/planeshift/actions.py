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
                         --datadir=%s \
                         --docdir=/usr/share/doc/%s \
                         --enable-optimize-mode-debug-info=no \
                         --with-optimize-debug-info=no \
                         --enable-separate-debug-info=no \
                         --enable-cpu-specific-optimizations=no \
                         --with-cs-prefix=/usr \
                         --with-cel-prefix=/usr \
                         --with-x \
                         --with-cal3d \
                         --with-bfd" % (datadir, get.srcTAG()))

def build():
    #pisitools.dosed("Jamconfig", "-O3", get.CXXFLAGS())

    # Let's only build client for now.
    shelltools.system("jam -aq client")

def install():
    shelltools.system("jam -s DESTDIR=%s install_bin" % get.installDIR())

    for data in ["data/npcbehave.xml", "data/npcdefs.xml", "data/pvp_regions.xml"]:
        pisitools.insinto("%s/data" % datadir, data)

    for f in ["eedit.cfg", "npcclient.cfg", "pslaunch.cfg", "psserver.cfg"]:
        pisitools.insinto(datadir, f)

    shelltools.copytree("lang", "%s/%s" % (get.installDIR(), datadir))
    shelltools.copytree("data/eedit", "%s/%s/data" % (get.installDIR(), datadir))
    shelltools.copytree("data/gui", "%s/%s/data" % (get.installDIR(), datadir))
    shelltools.copytree("art/music", "%s/%s/art" % (get.installDIR(), datadir))
    shelltools.copytree("art/runes", "%s/%s/art" % (get.installDIR(), datadir))

    pisitools.insinto("%s/art/world" % datadir, "art/world/sound.xml")
    pisitools.insinto("%s/art" % datadir, "art/racelib.xml")
    pisitools.insinto("%s/art" % datadir, "art/sfxfiles.dtd")

    pisitools.domove("/usr/bin/*", datadir)
    pisitools.removeDir("/usr/bin")

    pisitools.dohtml("docs/*.html")
    pisitools.dodoc("docs/*.txt")
