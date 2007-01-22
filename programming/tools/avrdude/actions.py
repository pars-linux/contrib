from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools


def setup():
    autotools.configure("--enable-doc")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("AUTHORS","NEWS","README","ChangeLog*")

