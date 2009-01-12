#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="HawkNL1.68"
flags="%s \
      -funroll-all-loops \
      -ffast-math \
      -D_GNU_SOURCE \
      -D_REENTRANT \
      -Wall \
      -fPIC" % get.CFLAGS()

def setup():
    shelltools.move("makefile.linux", "makefile")

def build():
    autotools.make('CC=%s \
                    CFLAGS="%s"' % (get.CC(), flags))

def install():
    pisitools.dodir("/usr/lib")
    pisitools.dodir("/usr/include")

    autotools.rawInstall("LIBDIR=%s/usr/lib INCDIR=%s/usr/include" % (get.installDIR(), get.installDIR()))

    # remove static library
    pisitools.remove("/usr/lib/libNL.a")

    pisitools.dodoc("samples/*/*")
