#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules

def setup():
    pythonmodules.run ("setup.py configure --no-install-init \
                                           --no-install-kde \
                                           --resume=/usr/share/wicd/scripts \
                                           --suspend=/usr/share/wicd/scripts \
                                           --verbose")

def build():
    pythonmodules.compile()

def install():
    pythonmodules.install()
