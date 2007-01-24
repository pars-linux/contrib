#!/usr/bin/python
#
#Ertugrul Erata ertugrulerata at gmail.com
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--enable-static=no")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("TODO", "README", "NEWS", "ChangeLog", "AUTHORS")
    pisitools.insinto("etc/xdg/xfce4/desktop", "menu.xml.tr")
    # conflict
    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")