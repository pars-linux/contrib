#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="%s-%s" % (get.srcNAME(), get.srcVERSION().replace('_', ''))

def build():
    autotools.make()

def install():
    autotools.install("DESTDIR=%s" % get.installDIR())

#    pisitools.remove("/usr/bin/listen")
    pisitools.remove("/usr/share/man/man1/listen.1.gz")

    pisitools.dodoc("README", "TODO", "copy", "gpl.txt")
