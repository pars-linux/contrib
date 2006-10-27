#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools


def setup():
    pass

def build():
    pass

def install():
    pisitools.doexe("icemergeprefs.py", "/usr/bin")
    pisitools.insinto("/usr/share/icemergeprefs", "icemergeprefs.png")
    pisitools.dodoc("README.icemergeprefs", "ChangeLog")