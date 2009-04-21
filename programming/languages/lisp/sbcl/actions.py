#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "sbcl-%s-x86-linux" % get.srcVERSION()

def install():
    shelltools.system("INSTALL_ROOT=%s/usr/ sh install.sh" % get.installDIR())

    pisitools.doman("sbcl.1")
    pisitools.dodoc("NEWS", "README", "CREDITS", "COPYING", "SUPPORT", "BUGS")
