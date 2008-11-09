#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-static \
                         --enable-speex \
                         --enable-lame \
                         --enable-tooltips \
                         --enable-mad \
                         --enable-ffmpeg")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/doc/idjc-%s/" % get.srcVERSION())

    pisitools.dodoc("AUTHORS", "COPYING", "ChangeLog", "NEWS", "README")
    pisitools.dohtml("doc/*")

