#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008, 2009  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "cinelerra"

def setup():
    shelltools.export("AUTOPOINT", "/bin/true")
    autotools.autoreconf("-fiv")

    autotools.configure("--enable-alsa \
                         --enable-mmx \
                         --with-external-ffmpeg \
                         --disable-opengl \
                         --enable-esd \
                         --disable-rpath \
                         --disable-static \
                         --with-buildinfo=cust/GIT\ Pardus\ build")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/include")

    pisitools.rename("/usr/bin/mpeg3cat", "mpeg3cat.hv")
    pisitools.rename("/usr/bin/mpeg3dump", "mpeg3dump.hv")
    pisitools.rename("/usr/bin/mpeg3toc", "mpeg3toc.hv")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "LICENSE", "NEWS", "TODO")
