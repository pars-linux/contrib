#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-static \
                         --enable-speex \
                         --enable-lame \
                         --enable-tooltips \
                         --enable-mad \
                         --enable-ffmpeg \
                         --docdir=/usr/share/doc/%s" % get.srcTAG())

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dohtml("doc/*")
