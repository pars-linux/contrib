#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def setup():
    kde.configure()

def build():
    shelltools.system("lrelease po/klearnnotes2_tr_TR.ts")

    kde.make()

def install():
    kde.install()

    pisitools.dodoc("TODO*", "README", "NEWS", "AUTHORS", "BUGS")
