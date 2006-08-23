from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "kalgebra"

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README", "TODO")