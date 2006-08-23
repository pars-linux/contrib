#
#Pardox pardox2006 at hotmail dot com
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.domo("streamtuner.po" , "tr" , "streamtuner.mo")
    pisitools.dodoc("AUTHORS", "COPYING", "INSTALL", "NEWS", "README", "TODO")