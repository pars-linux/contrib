#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

WorkDir="rpy-1.0-RC3"

def install():
    pythonmodules.install()

    pisitools.remove("/usr/lib/python2.4/site-packages/rpy_wintools.py")