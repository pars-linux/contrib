from pisi.actionsapi import autotools


WorkDir="Thunar-0.3.2beta2"

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