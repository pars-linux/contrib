#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

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
    pisitools.remove("/usr/kde/3.5/share/services/svn+*.protocol")
    pisitools.remove("/usr/kde/3.5/share/services/svn.protocol")