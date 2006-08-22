#
#Pardox pardox2006 at hotmail dot com
#

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
#from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "kino-0.8.1"

def setup():
    autotools.configure()
    
def build():
    autotools.make()
	
def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodoc("README", "ABOUT-NLS", "BUGS", "AUTHORS", "ChangeLog", "COPYING", "INSTALL", "NEWS", "TODO", "README_jogshuttle")