#
#Pardox pardox2006 at hotmail dot com
#


from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "/usr"

def setup():
    pisitools.dosed("bin/smc", "/usr/share/games/smc-0.96", "/usr/share/smclone")

def build():
    pass

def install():
    pisitools.dobin("bin/smc")
    pisitools.insinto("/usr/share/smclone/", "share/games/smc-0.96/*")
    shelltools.system("chmod 755 -R %s/usr/share/smclone" % get.installDIR())
