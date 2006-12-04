#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir="muParser"

def setup():
    autotools.configure("--enable-shared")

def build():
    autotools.make()


def install():
    autotools.install()