#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005-2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "qcad-%s-1-community.src" % get.srcVERSION()

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
    pisitools.dosed("qcad/Makefile", "../dxflib/lib/libdxf.a", "")

def build():
    modules = ["qcadlib", "qcadcmd", "qcadactions", "qcadguiqt", "qcad"]

    for i in modules:
        shelltools.cd("%s/src/" % i)
        shelltools.system("qmake %s.pro" % i)
        shelltools.cd("..")
        autotools.make()
        shelltools.cd("..")
        for lang in ["cs", "el", "fr", "nl", "ru", "da", "en", "hu", "sk", "de", "et", "it", "pl", "tr"]:
            shelltools.system("lrelease %s/src/ts/%s_%s.ts -qm %s/src/ts/%s_%s.qm" %(i, i, lang, i, i, lang))

def install():
    pisitools.dobin("qcad/qcad")

    for qm in ["qcadlib", "qcadcmd", "qcadactions", "qcadguiqt", "qcad"]:
        pisitools.insinto("/usr/share/qcad/qm", "%s/src/ts/*.qm" % qm)

    pisitools.insinto("/usr/share/qcad/fonts", "qcad/fonts/*.cxf")

    pisitools.dohtml("qcad/doc/*")
