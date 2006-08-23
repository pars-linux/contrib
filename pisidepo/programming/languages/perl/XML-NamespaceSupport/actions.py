#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Fethi Aymaz <fethi@linux-sevenler.org>

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