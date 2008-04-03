#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import kde

WorkDir= "kuftp-1.5.0-beta1"

def setup():
    kde.configure()

def build():
    kde.make()

def install():
    kde.install()
