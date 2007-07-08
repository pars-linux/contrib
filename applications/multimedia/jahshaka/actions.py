#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = 'jahshaka'

def setup():
    autotools.configure('--enable-openalframework')

def build():
    autotools.make()

def install():
    autotools.rawInstall('INSTALL_ROOT="%s"' % get.installDIR())

    pisitools.dodoc('COPYING', 'README', 'TODO')
