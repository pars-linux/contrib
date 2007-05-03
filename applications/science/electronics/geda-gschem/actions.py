#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
import os

WorkDir = "geda-gschem-%s" % get.srcVERSION()

def setup():
    autotools.configure()

def build():
    os.system("msgfmt -c -o po/tr.gmo po/tr.po")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS","ChangeLog","NEWS","README","TODO","VOCABULARY")
    pisitools.dosym("/usr/bin/gschem", "/usr/bin/geda")
