#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

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
    pisitools.domove("/bin","/usr/kde/3.5/bin/")
    pisitools.domove("/share/","/usr/kde/3.5/share")