#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-scrollkeeper \
                         --disable-schemas-install")

def build():
    autotools.make()

def install():
    autotools.install()

    # remove TR locale, it hasn't been translated completely
    pisitools.remove("/usr/share/locale/tr/LC_MESSAGES/gramps.mo")
    pisitools.dodoc("AUTHORS", "ChangeLog", "README","NEWS","FAQ","TODO")
