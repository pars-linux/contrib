#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.remove("/usr/lib/libsensors.a")

    pisitools.insinto("%s/%s" % (get.docDIR(),get.srcTAG()),"doc/*")
    pisitools.dodoc("CHANGES","CONTRIBUTORS","README")
