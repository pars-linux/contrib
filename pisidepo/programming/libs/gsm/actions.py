from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir="gsm-1.0-pl12"


def build():
    autotools.make()

def install():
    pisitools.dolib_a("lib/libgsm.a")
    pisitools.dobin("bin/*")
    pisitools.insinto("/usr/include","inc/gsm.h")
    pisitools.doman("man/*")
    pisitools.dodoc("COPYRIGHT","ChangeLog*","MACHINES","MANIFEST","README")