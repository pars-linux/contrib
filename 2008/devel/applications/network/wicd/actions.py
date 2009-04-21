#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

def setup():
    pythonmodules.run ("setup.py configure --no-install-init \
                                           --no-install-docs \
                                           --resume=/usr/share/wicd/scripts \
                                           --suspend=/usr/share/wicd/scripts \
                                           --verbose")

def install():
    pythonmodules.install()

    pisitools.dodoc ("AUTHORS", "CHANGES", "INSTALL", "LICENSE", "README")
