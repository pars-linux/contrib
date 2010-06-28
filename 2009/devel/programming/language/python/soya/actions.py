#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules
from pisi.actionsapi import get


WorkDir="Soya-0.15rc1"

def build():
    pythonmodules.compile()  
      
def install():
    pythonmodules.install()

    #remove soya_editor
    #pisitools.removeDir("/usr/bin")
    #pisitools.removeDir("/usr/lib/%s/site-packages/soya/editor" % get.curPYTHON())
