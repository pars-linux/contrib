#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()
    pisitools.insinto("/usr/share/pixmaps/", "src/gui/images/twinkle48.png", "twinkle.png")

    pisitools.dodoc("COPYING", "README", "ChangeLog", "AUTHORS", "NEWS", "TODO", "THANKS")
