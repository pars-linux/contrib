#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir="kadu"

def setup():
    autotools.configure("--enable-modules --enable-pheaders --enable-dist-info=Pardus")

def build():
    autotools.make()

def install():
    autotools.install()
    #This is included as an additional file in the correct directory
    pisitools.removeDir("/usr/share/applnk")

