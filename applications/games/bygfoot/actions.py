#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "bygfoot-%s-source" % get.srcVERSION()

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.insinto("/usr/share/pixmaps", "support_files/pixmaps/bygfoot_icon.png", "bygfoot.png")
    pisitools.insinto("/usr/share/applications", "bygfoot.desktop")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "ReleaseNotes", "INSTALL", "NEWS", "TODO", "UPDATE")
