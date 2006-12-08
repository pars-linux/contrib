#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import kde

WorkDir="LabPlot-1.5.1.5"

def setup():
    kde.configure("--enable-system-qwtplot3d --disable-KexiDB ")


def build():
    kde.make()



def install():
    kde.install()
    pisitools.remove("/usr/kde/3.5/bin/opj2dat")
    pisitools.remove("/usr/kde/3.5/lib/liborigin.*")