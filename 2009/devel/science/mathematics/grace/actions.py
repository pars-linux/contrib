#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.dosed("src/*", "doc/", "/usr/share/doc/%s/html/" % get.srcTAG())
    pisitools.dosed("src/xmgrace.c", "examples/", "/usr/share/doc/%s/examples/" % get.srcTAG())

    autotools.configure("--enable-grace-home=/usr/share/grace \
                         --with-helpviewer='firefox %s' \
                         --with-fftw \
                         --enable-netcdf \
                         --enable-jpegdrv \
                         --enable-pngdrv \
                         --enable-pdfdrv \
                         --enable-editres \
                         --disable-xmhtml")

def build():
    autotools.make()

def install():
    autotools.rawInstall("GRACE_HOME=%s/usr/share/grace \
                          PREFIX=%s/usr" % (get.installDIR(), get.installDIR()))

    pisitools.domove("/usr/share/grace/doc/*", "/usr/share/doc/%s/html" % get.srcTAG())
    pisitools.domove("/usr/share/grace/examples", "/usr/share/doc/%s" % get.srcTAG())

    pisitools.dodoc("ChangeLog", "CHANGES", "COPYRIGHT", "DEVELOPERS", "LICENSE", "README")

    pisitools.removeDir("/usr/share/grace/doc")
