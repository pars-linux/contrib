#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import perlmodules

WorkDir="Audio-1.029"

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def install():
    perlmodules.install()
