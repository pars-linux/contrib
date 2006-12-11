#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def build():
    shelltools.cd("src")
    autotools.make()

def install():
    pisitools.dobin("src/herrie")

    pisitools.dodoc("COPYING", "ChangeLog", "TODO", "README")
