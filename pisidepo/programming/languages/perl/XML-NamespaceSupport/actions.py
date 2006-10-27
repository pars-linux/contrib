#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import perlmodules


def setup():
    perlmodules.configure()

def build():
    perlmodules.make()
    perlmodules.make("test")

def install():
    perlmodules.install()
    pisitools.dodoc("Changes", "README", "MANIFEST")