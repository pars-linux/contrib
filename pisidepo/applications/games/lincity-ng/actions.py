#
#Pardox pardox2006 at hotmail dot com
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

#WorkDir = "lincity-ng-1.0.3"
NoStrip = "/"

def setup():
    autotools.configure("--enable-debug")

def build():
    shelltools.system("jam")


def install():
    shelltools.system("jam install")
    pisitools.dobin("lincity-ng")
    pisitools.dobin("xmlgettext")
    pisitools.dodoc("doc/COPYING*", "README",  "RELNOTES",  "TODO",  "userconfig.xml")
    pisitools.doman("doc/lincity-ng.6")
    pisitools.insinto("/usr/share/applications", "lincity-ng.desktop")
    pisitools.insinto("/usr/share/pixmaps", "data/lincity-ng.png")
    pisitools.insinto("/usr/share/lincity-ng", "data/*")

#   Jamfile clean up
    pisitools.remove("/usr/share/lincity-ng/Jamfile")
    pisitools.remove("/usr/share/lincity-ng/gui/Jamfile")
