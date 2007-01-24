#!/usr/bin/python
#
#Ertugrul Erata ertugrulerata at gmail.com
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("NOTES", "NEWS", "TODO", "README", "ChangeLog", "AUTHORS")
    # conflict
    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")