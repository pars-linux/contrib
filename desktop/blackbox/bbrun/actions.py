#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "bbrun-1.6/bbrun"

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dobin("bbrun")
    shelltools.cd("..")
    pisitools.dodoc("Changelog", "COPYING", "README")