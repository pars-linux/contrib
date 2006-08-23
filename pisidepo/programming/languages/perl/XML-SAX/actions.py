#
#Pardox pardox2006 at hotmail dot com
#

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import perlmodules

def setup():
#   local installvendorlib
#   eval $(perl '-V:installvendorlib')
#   unpack ${A}
#
#   sed -i -e "s,\(-MXML::SAX\),-I${D}/${installvendorlib} \1," ${S}/Makefile.PL  done as a patch
#
    perlmodules.configure()

def build():
    perlmodules.make("test")
    perlmodules.make()

def install():
    perlmodules.install()
    pisitools.dodoc("Changes", "LICENSE", "MANIFEST", "README")