#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

def setup():
    #Fix Contents(Help) Link
    pisitools.dosed("src/window.c", "\",PACKAGE,\"", "%s" % get.srcTAG())
    autotools.configure("--disable-debug \
                         --disable-static")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.removeDir("/usr/share/doc/xarchiver/")

    pisitools.dohtml("doc/html/*")
    pisitools.dodoc("AUTHORS", "NEWS", "README", "TODO", "ChangeLog", "COPYING")
