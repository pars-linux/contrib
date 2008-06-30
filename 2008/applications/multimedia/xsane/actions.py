#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("CXXFLAGS", "%s -I/usr/include/lcms" % get.CXXFLAGS())
    shelltools.export("LDFLAGS", "%s -L/usr/lib -llcms" % get.LDFLAGS())

    autotools.configure("--enable-gtk2 \
                         --enable-nls \
                         --enable-jpeg \
                         --enable-png \
                         --enable-tiff \
                         --enable-gimp \
                         --enable-lcms \
                         --disable-sanetest \
                         --disable-gimptest \
                         --disable-gtktest")

def build():
    autotools.make()


def install():
    autotools.install()

    # Make xsane symlink. Now, it is seen as a plugin in gimp.
    pisitools.dosym("/usr/bin/xsane", "/usr/lib/gimp/2.0/plug-ins/xsane")

    pisitools.dodoc("xsane.*")

    pisitools.removeDir("/usr/sbin")
