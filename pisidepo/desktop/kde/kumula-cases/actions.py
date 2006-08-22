#!/usr/bin/python
#
#Ertugrul Erata ertugrulerata at gmail.com
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="kumula"

def setup():
    pass

def build():
    pass


def install():
    pisitools.dobin("bin/*", "opt/kumula/bin")
    pisitools.insinto("/opt/kumula/lib","lib/*")
    pisitools.insinto("/opt/kumula/graphics","graphics/*")
    pisitools.insinto("/opt/kumula/sql","sql/*")