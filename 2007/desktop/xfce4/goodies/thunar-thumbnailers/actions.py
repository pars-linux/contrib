#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2005  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir="thunar-thumbnailers-0.0.1svn-r02563"

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()
    
    pisitools.dodoc("NEWS", "README", "AUTHORS", "ChangeLog")
