#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from os import path, walk
from pisi.actionsapi import autotools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

def fixperms(d):
    for root, dirs, files in walk(d):
        for name in dirs:
            shelltools.chmod(path.join(root, name), 0755)
        for name in files:
            shelltools.chmod(path.join(root, name), 0644)

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install("INSTALL_ROOT=%s" % get.installDIR())
    fixperms("%s/usr/share/pdfedit" % get.installDIR())

