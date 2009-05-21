#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools

WorkDir="k3d-source-%s" % get.srcVERSION()

def setup():
    shelltools.unlink("CMakeCache.txt")
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-DK3D_BUILD_GNOME_MODULE=OFF \
                          -DK3D_BUILD_AQSIS_MODULE=ON \
                          -DK3D_BUILD_PARALLEL=OFF", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    #Use Pardus' Bitstream-Vera-fonts package
    pisitools.removeDir("/usr/share/k3d/fonts/")

    pisitools.dosym( "/usr/share/k3d/icons/k3d.png", "/usr/share/pixmaps/k3d.png")

    pisitools.dodoc("../AUTHORS", "../COPYING", "../README")
