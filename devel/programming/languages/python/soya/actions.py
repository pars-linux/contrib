#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

WorkDir="Soya-0.13"

def install():
    pythonmodules.install()
    pythonmodules.fixCompiledPy()

    #remove soya_editor
    pisitools.remove("/usr/bin/soya_editor")
    pisitools.removeDir("/usr/lib/python2.4/site-packages/soya/editor")
