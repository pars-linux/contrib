#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "Amaya11.2/Amaya"

def setup():
    # Cleanup crap
    shelltools.unlinkDir("../libwww")
    shelltools.unlinkDir("../freetype")
    shelltools.unlinkDir("../Mesa")
    shelltools.unlinkDir("../redland")
    shelltools.unlinkDir("../wxWidgets")

    # Create a build directory for Pardus
    shelltools.makedirs("Pardus")
    shelltools.cd("Pardus")

    shelltools.system("ln -s ../configure")

    autotools.configure("--prefix=/usr/share \
                         --enable-system-libwww \
                         --enable-system-raptor \
                         --enable-system-wx \
                         --with-gl \
                         --with-dav \
                         --enable-svg \
                         --enable-annot \
                         --enable-templates \
                         --enable-generic-xml")

def build():
    shelltools.cd("Pardus")
    autotools.make("-j1 CFLAGS='%s' CXXFLAGS='%s'"
                   % (get.CFLAGS(), get.CXXFLAGS()))

def install():
    pisitools.insinto("/usr/share/pixmaps", "resources/bundle/logo.png", "amaya.png")

    shelltools.cd("Pardus")
    autotools.install("prefix=%s/usr/share" % get.installDIR())

    pisitools.domove("/usr/share/bin", "/usr")

    pisitools.dodoc("../README*")