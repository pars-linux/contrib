#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="autopano-sift-2.4/src"

def build():
    shelltools.export("MONO_SHARED_DIR", get.workDIR())
    autotools.make()

def install():
    pisitools.insinto("/usr/bin","bin/*.exe")
    pisitools.insinto("/usr/bin/","bin/autopano-complete.sh")
    pisitools.insinto("/usr/lib/","bin/ICSharpCode.SharpZipLib.dll")

    pisitools.doman("../doc/*.1")
    pisitools.insinto("/usr/share/doc/%s" % get.srcTAG(), "../doc/*.txt")
