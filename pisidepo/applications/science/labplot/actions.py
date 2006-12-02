#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="LabPlot-1.5.1.4"

def setup():
    autotools.configure("--enable-system-qwtplot3d --disable-KexiDB")


def build():
    autotools.make()



def install():
    autotools.install()
    pisitools.remove("/usr/bin/opj2dat")
    pisitools.remove("/usr/lib/liborigin.*")