#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="spearfish60"

def setup():
    pass

def build():
    pass

def install():
    pisitools.dodir("/opt/grass-6.2.0RC1/samples")
    pisitools.insinto("/opt/grass-6.2.0RC1/samples", "*")
