#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import autotools

WorkDir="texvc-linux-x86-20050202/src"

def build():
    autotools.make()


def install():
    pisitools.dobin("texvc")
    pisitools.dobin("texvc_test")
    pisitools.dobin("texvc_tex")