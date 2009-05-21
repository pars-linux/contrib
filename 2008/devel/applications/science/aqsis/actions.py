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

WorkDir="aqsis-1.5.0"
shelltools.export("HOME", "%s" % get.workDIR())

def setup():
    shelltools.makedirs("build")
    shelltools.cd("build")

    cmaketools.configure("-Wno-dev \
                          -DAQSIS_USE_RPATH:BOOL=OFF \
                          -DAQSIS_USE_FLTK:BOOL=ON \
                          -DAQSIS_FLTK_INCLUDE_DIR:PATH=/usr/include/FL \
                          -DAQSIS_FLTK_LIBRARIES_DIR:PATH=/usr/lib \
                          -DAQSIS_USE_OPENEXR:BOOL=ON \
                          -DAQSIS_BOOST_LIB_SUFFIX:STRING=-mt \
                          -DAQSIS_ENABLE_TESTING:BOOL=OFF \
                          -DAQSIS_USE_PLUGINS:BOOL=ON \
                          -DAQSIS_USE_TIMERS:BOOL=ON \
                          -DSYSCONFDIR:STRING=/etc \
                          -DLIBDIR=/usr/lib \
                          -DDEFAULT_DISPLAYPATH=/usr/lib/aqsis", sourceDir="..")

def build():
    shelltools.cd("build")
    cmaketools.make()

def install():
    shelltools.cd("build")
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("../AUTHORS", "../COPYING", "../README", "../ReleaseNotes")
