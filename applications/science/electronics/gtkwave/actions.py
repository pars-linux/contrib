from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools


def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("ANALOG_README.TXT","CHANGELOG.TXT")

