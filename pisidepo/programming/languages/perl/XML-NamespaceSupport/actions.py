#
#Pardox pardox2006 at hotmail dot com
#

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import get


def setup():
    perlmodules.configure()

def build():
    perlmodules.make()
    perlmodules.make("test")

def install():
    perlmodules.install()
    pisitools.dodoc("Changes", "README", "MANIFEST")