#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

docdir="%s/%s" % (get.docDIR(), get.srcTAG())

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --qtdir=/usr/qt/4 \
                            --disable-bundled-qca")

def build():
    autotools.make()

def install():
    autotools.rawInstall('INSTALL_ROOT="%s"'  % get.installDIR())

    pisitools.domove("/usr/share/psi/README", "%s" % docdir)
    pisitools.domove("/usr/share/psi/COPYING", "%s" % docdir)
