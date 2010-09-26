#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools


def setup():
    shelltools.export("AUTOPOINT", "true")
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --enable-nls \
                         --enable-startup-notification \
                         --docdir=/%s/%s" % (get.docDIR(), get.srcNAME()))

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "CHANGELOG", "COPYING", "README")
