#
#Pardox pardox2006 at hotmail dot com
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "uae-0.8.25"

def setup():
    autotools.configure()

def install():
    autotools.make()
    pisitools.dobin("uae")
    pisitools.dobin("readdisk")
    pisitools.insinto("/usr/share/uae/amiga-tools", "amiga/*hack")
    pisitools.insinto("/usr/share/uae/amiga-tools", "amiga/trans*")
    pisitools.insinto("/usr/share/uae/amiga-tools", "amiga/uae*")
    pisitools.dodoc("docs/unix/README", "docs/*", "COPYING")