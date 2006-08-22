#
# PardoX Pardox at hotmail dot com
#


from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    pass

def build():
    shelltools.cd("src")
    autotools.make()
    shelltools.cd("..")

def install():
    pisitools.dobin("src/rawrec")
    pisitools.dobin("src/rawplay")
    pisitools.doman("docs/user/rawrec.1")
    pisitools.dodoc("docs/programmer/*", "ChangeLog", "copyright", "INSTALL")