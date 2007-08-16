#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.system("sh Configure config/urt")
    shelltools.unlink("bin/README")

def build():
    autotools.make("DEST=/usr")

def install():
    pisitools.dodir("/usr/bin")
    autotools.rawInstall("DEST=%s/usr/bin" % get.installDIR())

    pisitools.domove("/usr/bin/librle.*","/usr/lib")
    pisitools.domove("/usr/bin/*.h","/usr/include")

    pisitools.insinto("/usr/share/man","man/man*")
    pisitools.dodoc("*-changes","CHANGES*","README","blurb")

    # remove conflicting manpage
    pisitools.remove("/usr/share/man/man1/template.1")
