#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def setup():
    autotools.configure("--with-zip \
                         --with-jpeg \
                         --with-libtiff \
                         --with-proj \
                         --disable-static")

def build():
    shelltools.export("LDFLAGS", "")
    autotools.make()

def install():
    autotools.install()

    pisitools.remove("/usr/lib/libgeotiff.a")

    pisitools.dodoc("ChangeLog", "Doxyfile", "HOWTO-RELEASE", "LICENSE", "README*", "docs/manual.txt")
    pisitools.dohtml("docs/*")
    pisitools.remove("/usr/share/doc/%s/README.WIN" % get.srcTAG())

