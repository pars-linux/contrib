from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="FTGL/unix"

def setup():
    shelltools.system("/usr/bin/autoreconf")
    shelltools.system("/usr/bin/libtoolize --copy --force")
    autotools.configure("--with-gl-lib=/usr/lib --enable-shared")

def build():
    autotools.make()

def install():
    autotools.install()