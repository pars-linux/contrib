#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    pass

def build():
    autotools.make("prefix=/usr")

def install():
    autotools.rawInstall("prefix=%s/usr" % get.installDIR())
    pisitools.domove("/usr/man", "/usr/share/man")
    pisitools.dohtml("manual*.html")
    pisitools.dodir("/var/tmp/nxtvdb")
    pisitools.dodoc("CHANGES", "COPYRIGHT", "README*", "TODO")