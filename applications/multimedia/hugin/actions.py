#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools

WorkDir="hugin-0.7-beta1"

def setup():
    autotools.configure("--enable-shared \
                         --disable-static \
                         --with-unicode \
                         --disable-desktop")

def build():
    autotools.make()

def install():
    autotools.install()
