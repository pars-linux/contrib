#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

WorkDir='mysql-gui-tools-5.0r12'

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.cd('mysql-gui-common')
    autotools.configure('--enable-grt --enable-canvas')

def build():
    shelltools.cd('mysql-gui-common')
    autotools.make()

def install():
    shelltools.cd('mysql-gui-common')
    autotools.install()
    pisitools.dodoc("COPYING", "README.translating")
