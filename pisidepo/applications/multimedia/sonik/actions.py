#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde
from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools

def setup():
    kde.configure()

def build():
    shelltools.system("autoheader")
    autotools.autoconf()
    kde.make()

def install():
    kde.install()