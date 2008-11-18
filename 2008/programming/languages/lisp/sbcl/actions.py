#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "sbcl-%s-x86-linux" % get.srcVERSION()

def setup():
    # for correct doc directory : /usr/share/doc/sbcl-{srcVERSION}
    pisitools.dosed("install.sh", '/share/doc/sbcl}', '/share/doc/sbcl-%s}' % get.srcVERSION())

def build():
    pass

def install():
    install_root = "%s/usr" % get.installDIR()
    shelltools.system("SBCL_HOME=\"\" INSTALL_ROOT=%s sh install.sh" % install_root)
