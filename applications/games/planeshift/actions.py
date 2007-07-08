#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "planeshift"
datadir = "/usr/share/planeshift"

def setup():
    shelltools.system("./autogen.sh")

    autotools.configure("--disable-debug \
                         --without-separate-debug-info \
                         --enable-cpu-specific-optimizations=no \
                         --with-cs-prefix=/usr \
                         --with-cel-prefix=/usr \
                         --with-x \
                         --with-Xaw \
                         --with-Xxf86vm \
                         --with-cal3d \
                         --without-bfd")

def build():
    pisitools.dosed("Jamconfig", "-O3", get.CFLAGS())

    # Let's only build client for now.
    shelltools.system("jam -aq client")

def install():
    pisitools.dodir("%s/data" % datadir)
    shelltools.system("jam -s DESTDIR=%s install_bin" % get.installDIR())

    shelltools.copytree("lang", "%s/%s" % (get.installDIR(), datadir))

    pisitools.domove("/usr/bin/*", datadir)
    pisitools.removeDir("/usr/bin")

    shelltools.copytree("data/eedit", "%s/%s/data/" % (get.installDIR(), datadir))
    shelltools.copytree("data/partview", "%s/%s/data/" % (get.installDIR(), datadir))
    shelltools.copytree("data/pawseditor", "%s/%s/data/" % (get.installDIR(), datadir))
    shelltools.copytree("data/schemas", "%s/%s/data/" % (get.installDIR(), datadir))

    pisitools.dosed("planeshift.cfg", "Video.FullScreen = false", "Video.FullScreen = true")
    pisitools.dosed("psclient.cfg", "cvs", "elves")

    pisitools.insinto(datadir, "*.cfg")

    pisitools.dosym("/usr/share/fonts/dejavu/DejaVuSerif.ttf", "%s/data/ttf/arial.ttf" % datadir)

    pisitools.dodoc("docs/*.txt")
    pisitools.dohtml("docs/*")
