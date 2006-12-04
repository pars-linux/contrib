

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir="Thunar-0.5.0rc2"

def setup():
    autotools.configure("--enable-dbus \
                         --disable-gnome-thumbnailers \
                         --enable-startup-notification \
                         --with-volume-manager=hal \
                         ")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")