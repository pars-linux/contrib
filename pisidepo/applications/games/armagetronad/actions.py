#Murat Şenel
#
#murattsenell@gmail.com

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():

    shelltools.export("XML2_CONFIG", "xml2-config")
    autotools.configure("--enable-master \
                         --enable-main \
                         --disable-music \
                         --enable-sysinstall \
                         --enable-etc \
                         --enable-desktop \
                         --enable-initscripts=/etc/init.d \
                         --enable-glout \
                         --with-x")

def build():
    autotools.make()


def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README*")
    pisitools.dohtml("src/doc/*.html")
    pisitools.remove("/usr/bin/armagetronad-uninstall")