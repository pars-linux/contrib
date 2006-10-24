#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 Rajeev J Sebastian, rajeev.sebastian@gmail.com
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
from pisi.actionsapi import kde

def setup():
    kde.configure()

def build():
    #autotools.make()
    kde.make()

def install():
    kde.install()
    pisitools.dodoc("AUTHORS", "BUGS", "NEWS", "README*", "TODO", "THANKS")
