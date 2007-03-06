#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import kde
from pisi.actionsapi import shelltools



def setup():
    shelltools.system("cmake -DCMAKE_INSTALL_PREFIX=%s" % (get.kdeDIR()))


def build():
    kde.make()


def install():
    kde.install()
    #remove files conflicts kdesvn
    pisitools.remove("/usr/kde/3.5/share/services/svn+file.protocol")
    pisitools.remove("/usr/kde/3.5/share/services/svn+http.protocol")
    pisitools.remove("/usr/kde/3.5/share/services/svn+https.protocol")
    pisitools.remove("/usr/kde/3.5/share/services/svn+ssh.protocol")
    pisitools.remove("/usr/kde/3.5/share/services/svn.protocol")