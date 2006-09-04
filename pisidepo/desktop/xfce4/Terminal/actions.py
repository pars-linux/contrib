from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir="Terminal-0.2.5.4beta2"

def setup():
    autotools.configure("--enable-dbus")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")
    pisitools.removeDir("/usr/share/doc/Terminal/ja")