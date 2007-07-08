#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="geda-gschem-%s" % get.srcVERSION().split('_')[-1]

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.domo("po/tr.po", "tr", "geda-gschem.mo")
    pisitools.dosym("/usr/bin/gschem", "/usr/bin/geda")

    pisitools.dodoc("AUTHORS","ChangeLog","NEWS","README","TODO","VOCABULARY")
