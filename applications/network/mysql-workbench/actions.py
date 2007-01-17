#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

WorkDir='mysql-gui-tools-5.0r8'

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    shelltools.cd('mysql-gui-common')
    autotools.configure('--enable-grt --enable-canvas')
    shelltools.cd('../mysql-workbench')
    autotools.configure('--enable-python-modules')

def build():
    shelltools.cd('mysql-gui-common')
    autotools.make()
    shelltools.cd('../mysql-workbench')
    autotools.make()

def install():
    shelltools.cd('mysql-workbench')
    autotools.install()
    pisitools.dodoc('COPYING', 'ChangeLog')
