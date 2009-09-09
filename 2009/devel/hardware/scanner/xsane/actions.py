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
    autotools.configure("--enable-gtk2 \
                         --enable-nls \
                         --enable-jpeg \
                         --enable-png \
                         --enable-tiff \
                         --enable-gimp \
                         --enable-lcms")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # Make xsane symlink. Now, it is seen as a plugin in gimp.
    pisitools.dosym("/usr/bin/xsane", "/usr/lib/gimp/2.0/plug-ins/xsane")

    pisitools.dodoc("xsane.*")

    pisitools.removeDir("/usr/sbin")

