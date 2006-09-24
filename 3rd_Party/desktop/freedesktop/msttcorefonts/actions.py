#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="msttcorefonts"

def install():
    pisitools.dodir("/usr/share/fonts/msttcorefonts/");
    shelltools.copy("*.ttf","%s/usr/share/fonts/msttcorefonts/" % get.installDIR());

    pisitools.dodoc("eula.htm")
