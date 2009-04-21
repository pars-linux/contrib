#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
   pisitools.dobin("checkgmail")
   #pisitools.doman("man/checkgmail.1.gz") //going to be fixed, follow the bug #8426

   pisitools.dodoc("Readme", "copying", "ChangeLog", "todo")

