#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

WorkDir='mysql-gui-tools-5.0r9'

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.cd('mysql-gui-common')
    autotools.configure()
    shelltools.cd('../mysql-administrator')
    autotools.configure()

def build():
    shelltools.cd('mysql-gui-common')
    autotools.make()
    shelltools.cd('../mysql-administrator')
    autotools.make()

def install():
    shelltools.cd('mysql-administrator')
    autotools.install()
    pisitools.dodoc('COPYING', 'ChangeLog')
