#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def build():
    shelltools.export("CHECK_DEPENDS", "0")
    shelltools.export("USE_GTK_MOZEMBED", "1")
    shelltools.export("GTK_MOZEMBED_PATH", "/usr/lib/%s/site-packages/gtk-2.0/gtkmozembed.so" % get.curPYTHON())
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/bin/listen")
    pisitools.remove("/usr/share/man/man1/listen.1.gz")

    pisitools.dodoc("README", "TODO", "copy", "gpl.txt")
