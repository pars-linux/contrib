#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import scons
from pisi.actionsapi import kde
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def setup():
    shelltools.system("/usr/bin/python configure")

def build():
    scons.make()

def install():
    kde.install()
    pisitools.domove("/bin","/usr/kde/3.5/")
    pisitools.domove("/share/","/usr/kde/3.5/share")

    pisitools.dodoc("AUTHORS", "COPYING", "README")
