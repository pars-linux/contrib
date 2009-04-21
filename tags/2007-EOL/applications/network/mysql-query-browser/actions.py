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
    autotools.configure()

    shelltools.cd('../mysql-query-browser')
    pisitools.dosed('configure', 'gtkhtml=libgtkhtml-3.0', 'gtkhtml=libgtkhtml-3.14')  # fix gtkhtml version check
    autotools.configure()

def build():
    shelltools.cd('mysql-gui-common')
    autotools.make()

    shelltools.cd('../mysql-query-browser')
    autotools.make()

def install():
    shelltools.cd('mysql-query-browser')
    autotools.install()

    pisitools.dodoc('COPYING', 'ChangeLog')
