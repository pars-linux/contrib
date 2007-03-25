#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools



def setup():
    shelltools.cd("configure")
    shelltools.system("python configure.py --disable-numarray -I /usr/qt/4/include/qwt/")


def build():
    shelltools.cd("configure")
    autotools.make()



def install():
    shelltools.cd("configure")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())