#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="GConf-%s" % get.srcVERSION()

def setup():
    autotools.configure("--enable-debug=yes --enable-static=no")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("README", "TODO", "NEWS", "ChangeLog", "AUTHORS")
