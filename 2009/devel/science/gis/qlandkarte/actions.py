#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = 'QLandkarte_%s' % get.srcVERSION()

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall('INSTALL_ROOT="%s"' % get.installDIR())

    pisitools.dodoc("skin/README.SKIN", "skin/skin.txt")
