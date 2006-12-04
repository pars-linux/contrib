#!/usr/bin/python
#
#Ertugrul Erata ertugrulerata at gmail.com
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir="exo-0.3.1.12rc2"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.insinto("/usr/libexec","exo-helper/exo-helper-0.3")
    pisitools.removeDir("/usr/share/xfce4/doc/ja")
    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")