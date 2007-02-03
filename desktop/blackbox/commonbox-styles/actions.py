#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools

def install():
    pisitools.insinto("/usr/share/commonbox/backgrounds", "backgrounds/*")
    pisitools.insinto("/usr/share/commonbox/styles", "styles/*")
    pisitools.dodoc("README.commonbox-styles", "COPYING", "STYLES.authors")
