#
#Pardox pardox2006 at hotmail dot com
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "cdogs-sdl-2006-03-27/src"

def setup():
    pass

def build():
    pisitools.dosed("Makefile", "/usr/local", "/usr")
    pisitools.dosed("Makefile", "/games/bin/", "/bin")
    pisitools.dosed("Makefile", "/share/games/cdogs/", "/share/cdogs/")
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dosym("/usr/share/cdogs/data/cdogs_icon.png", "/usr/share/pixmaps/cdogs.png")
#   pisitools.insinto("/usr/share/pixmaps/", "../data/cdogs_icon.png", "cdogs.png")
    pisitools.dodoc("../doc/*", "BIG_FAT_NOTE")
