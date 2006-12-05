#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="autopano-sift-2.4/src"

def build():
    autotools.make()

def install():
    pisitools.insinto("/usr/bin","bin/*.exe")
    pisitools.insinto("/usr/bin/","bin/autopano-complete.sh")
    pisitools.insinto("/usr/lib/","bin/ICSharpCode.SharpZipLib.dll")