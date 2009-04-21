#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    shelltools.system("qmake-qt4 fet.pro")

def build():
    autotools.make()

def install():
    pisitools.dobin("fet")

    pisitools.insinto("/usr/share/fet/sample_inputs","sample_inputs/*")
    pisitools.insinto("/usr/share/fet/translations","translations/*.qm")
    pisitools.insinto("/usr/share/fet/doc","doc/*")

    pisitools.remove("/usr/share/fet/doc/fet.1")

    pisitools.doman("doc/fet.1")
    pisitools.dodoc("AUTHORS", "ChangeLog", "CONTRIBUTORS", "COPYING", "GUESTBOOK",
    "LINKS", "README", "REFERENCES", "SPONSORS", "THANKS", "TODO", "TRANSLATORS")
