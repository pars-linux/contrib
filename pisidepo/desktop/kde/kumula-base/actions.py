#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="kumula"

def setup():
    pass

def build():
    pass


def install():
    pisitools.dobin("bin/*", "opt/kumula/bin")
    pisitools.insinto("/opt/kumula/lib","lib/*")
    pisitools.insinto("/opt/kumula/graphics","graphics/*")
    pisitools.insinto("/opt/kumula/i18n","i18n/*")
    pisitools.insinto("/opt/kumula/doc","doc/*")
    pisitools.insinto("/opt/kumula/sql","sql/*")