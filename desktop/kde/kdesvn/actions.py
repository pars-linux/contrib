#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import cmaketools



def setup():
    cmaketools.configure(installPrefix = "%s" % (get.kdeDIR()))


def build():
    cmaketools.make()


def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
    #remove files conflicts kdesvn
    pisitools.remove("/usr/kde/3.5/share/services/svn+file.protocol")
    pisitools.remove("/usr/kde/3.5/share/services/svn+http.protocol")
    pisitools.remove("/usr/kde/3.5/share/services/svn+https.protocol")
    pisitools.remove("/usr/kde/3.5/share/services/svn+ssh.protocol")
    pisitools.remove("/usr/kde/3.5/share/services/svn.protocol")