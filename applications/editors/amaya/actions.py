#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "Amaya%s/Amaya" % get.srcVERSION()

def setup():
    # Cleanup crap
    shelltools.unlinkDir("../libwww")
    shelltools.unlinkDir("../freetype")
    shelltools.unlinkDir("../Mesa")
    shelltools.unlinkDir("../redland")
    shelltools.unlinkDir("../wxWidgets")

    # Re-create configure file for system libs
    autotools.autoconf()

    # Create a build directory for Pardus
    shelltools.makedirs("Pardus")
    shelltools.cd("Pardus")

    shelltools.system("ln -s ../configure")

    autotools.configure("--enable-bookmarks \
                         --enable-templates \
                         --enable-system-libwww \
                         --enable-system-wx \
                         --enable-system-redland \
                         --enable-annot \
                         --with-dav \
                         --enable-svg \
                         --enable-generic-xml \
                         --without-graphiclibs")

def build():
    shelltools.cd("Pardus")
    autotools.make()

def install():
    pisitools.insinto("/usr/share/pixmaps", "resources/bundle/logo.png", "amaya.png")

    shelltools.cd("Pardus")
    pisitools.dodir("/usr/share")

    autotools.install()

    pisitools.domove("/usr/Amaya", "/usr/share/")

    pisitools.dosed("%s/usr/share/Amaya/wx/bin/amaya" % get.installDIR(), "usr", "usr/share")
    pisitools.domove("/usr/share/Amaya/wx/bin/amaya", "/usr/bin")
