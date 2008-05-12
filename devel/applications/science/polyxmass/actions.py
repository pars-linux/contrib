#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "polyxmass-bin-%s" % get.srcVERSION()

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.domove("/usr/share/applications/polyxmass-bin.desktop" , "/usr/share/applications/" ,  "polyxmass.desktop")
    pisitools.domove("/usr/share/pixmaps/polyxmass-icon-32x32.png" , "/usr/share/pixmaps/" ,  "polyxmass.png")

    pisitools.dodoc("COPYING", "README", "ChangeLog", "NEWS", "AUTHORS")
