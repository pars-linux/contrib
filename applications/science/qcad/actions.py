#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "qcad-2.0.5.0-1-community.src"

def setup():
    shelltools.echo("defs.pro", "DEFINES += _REENTRANT QT_THREAD_SUPPORT")
    shelltools.echo("defs.pro", "CONFIG += thread release")
    shelltools.echo("defs.pro", "QMAKE_CFLAGS_RELEASE = %s" % get.CFLAGS())
    shelltools.echo("defs.pro", "QMAKE_CXXFLAGS_RELEASE = %s" % get.CFLAGS())

    pisitools.dosed("mkspecs/defs.pro", "QMAKE_CXXFLAGS_DEBUG \+= -pedantic", "")
    pisitools.dosed("mkspecs/defs.pro", "QMAKE_CXXFLAGS \+= -pedantic", "")
    pisitools.dosed("qcadlib/src/Makefile",
                    "CXXFLAGS = .*",
                    "%s -DRS_NO_COMPLEX_ENTITIES -DQT_NO_DEBUG -DQT_SHARED \
                    -DQT_TABLET_SUPPORT -DQT_THREAD_SUPPORT" % get.CFLAGS())

    pisitools.dosed("qcadlib/src/qcadlib.pro", "INCLUDEPATH \+= (.*)", "INCLUDEPATH += \\1 ../../qcadcmd/src")

def build():
    modules = ["qcadlib", "qcadcmd", "qcadactions", "qcadguiqt", "qcad"]
    
    shelltools.cd("fparser/")
    autotools.configure()
    autotools.make()
    shelltools.cd("../")
    
    shelltools.cd("dxflib/")
    autotools.configure()
    autotools.make()
    shelltools.cd("../")

    for i in modules:
        shelltools.cd("%s/src/" % i)
        shelltools.system("qmake %s.pro" % i)
        shelltools.cd("../")
        autotools.make()
        shelltools.cd("../")

def install():
    pisitools.dobin("qcad/qcad")
