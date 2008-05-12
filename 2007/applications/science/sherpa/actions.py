#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "SHERPA-MC-%s" % get.srcVERSION()

def install():
    shelltools.system("TOOLS/makeinstall -c --copt --prefix=%s/usr" % get.installDIR())
