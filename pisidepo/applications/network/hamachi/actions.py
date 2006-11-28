#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

WorkDir="hamachi-0.9.9.9-20-lnx"

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools


def setup():
    pass

def build():
    shelltools.system("rm tuncfg/tuncfg")
    autotools.make()

def install():
    pisitools.dobin("hamachi")
    pisitools.dosbin("tuncfg/tuncfg")
    pisitools.dodoc("README","LICENSE")