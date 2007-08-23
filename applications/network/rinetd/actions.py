#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir= "rinetd"

def build():
    autotools.make()

def install():
    pisitools.dosbin("rinetd")

    pisitools.doman("rinetd.8")
    pisitools.dodoc("CHANGES", "README")
