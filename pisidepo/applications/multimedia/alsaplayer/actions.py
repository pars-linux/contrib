#
#Pardox pardox2006 at hotmail dot com
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    autotools.configure("--prefix=/usr")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("docs/wishlist.txt", "docs/donations.txt", "AUTHORS", "ChangeLog", "COPYING", "INSTALL", "README", "TODO")