#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

def install():
    for data in ["wink","Backgrounds","Buttons","Callouts","FlashControlBars","FlashPreloaders","Resources","Samples","Templates"]:
        pisitools.insinto("/usr/share/wink",data)

    pisitools.dodoc("Docs/*","changelog.txt","license.txt","readme.txt")
