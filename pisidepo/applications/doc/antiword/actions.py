#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    pass

def build():
    autotools.make()

def install():
    shelltools.system("make global_install DESTDIR=%s" % get.installDIR())
    pisitools.doman("Docs/antiword.1")
    shelltools.cd("Docs")
    pisitools.dodoc("COPYING","ChangeLog","Exmh","Emacs","FAQ","History","Netspace","ReadMe","Mozilla","Mutt","QandA")