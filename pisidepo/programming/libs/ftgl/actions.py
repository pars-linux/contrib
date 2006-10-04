from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir="FTGL/unix"

def setup():
    autotools.configure("--enable-shared \
                         --with-x")

def build():
    autotools.make()

def install():
    autotools.install()