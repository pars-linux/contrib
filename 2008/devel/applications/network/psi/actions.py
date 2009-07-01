#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir='psi-0.13-rc2'

def setup():
    autotools.rawConfigure("--prefix=/usr \
                            --qtdir=/usr/qt/4 \
                            --disable-bundled-qca")

def build():
    autotools.make()

def install():
    autotools.rawInstall('INSTALL_ROOT="%s"'  % get.installDIR())

    pisitools.dodoc("README","COPYING")
