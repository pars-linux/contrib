#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir = "bblaunch-0.0.3"

def setup():
    autotools.configure()
def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS", "CHANGELOG", "INSTALL", "LICENSE", "README")