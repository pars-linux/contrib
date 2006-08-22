#
#Pardox pardox2006 at hotmail dot com
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "lives-0.9.6-pre3"

def setup():
    autotools.configure("--prefix=/usr")

def build():
    autotools.make()

def install():
    autotools.install()