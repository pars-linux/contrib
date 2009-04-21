#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="cmus"
contrib = "%s/%s/contrib" % (get.docDIR(), get.srcTAG())

def setup():
    pisitools.dosed("configure","/doc/cmus/examples", "/doc/%s/examples" % get.srcTAG())
    shelltools.chmod("contrib/*", 0644)
    autotools.rawConfigure("prefix=/usr")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto(contrib, "contrib/*")
    pisitools.dodoc("AUTHORS", "COPYING", "README", "Doc/*.txt")
