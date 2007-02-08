#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import kde

WorkDir = "kbfx-0.4.9.2rc4"

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()

