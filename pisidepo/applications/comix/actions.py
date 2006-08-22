#
#Pardox pardox2006 at hotmail dot com
#

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    pass

def build():
    pass

def install():
#   pythonmodules.install("install --no-mime --installdir %s/usr 1>/dev/null" % get.installDIR())
#   shelltools.system("python install.py install --no-mime --installdir %s/usr 1>/dev/null" % get.installDIR())
    pisitools.insinto("/usr/share/mime/packages/", "mime/comix.xml")
    pisitools.insinto("/etc/gconf/schemas/", "mime/comicbook.schemas")
    pisitools.dobin("mime/comicthumb")
#   pisitools.doman("comix.1.gz", "mime/comicthumb.1.gz")
#   pisitools.insinto("/usr/share/pixmaps/", "images/comix.png")
#   pisitools.insinto("/usr/share/applications/", "comix.desktop")
    shelltools.system("python install.py install --no-mime --installdir %s/usr 1>/dev/null" % get.installDIR())
    pisitools.dodoc("ChangeLog", "COPYING", "README")
