#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt


from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def build():
    shelltools.cd("src")
    autotools.make()
    shelltools.cd("..")

def install():
    pisitools.dobin("src/rawrec")
    pisitools.dobin("src/rawplay")

    pisitools.doman("docs/user/rawrec.1")

    pisitools.dodoc("docs/programmer/*", "ChangeLog", "copyright")
