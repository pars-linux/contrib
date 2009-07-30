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
    shelltools.export("AUTOPOINT", "/bin/true")
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --enable-nls \
                         --enable-pam \
                         --disable-rpath \
                         --with-x")
def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domo("po/tr.po", "tr", "enlightenment.mo")

    pisitools.dodoc("AUTHORS", "COPYING", "README")
