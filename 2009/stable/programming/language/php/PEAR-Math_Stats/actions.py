#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="Math_Stats-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/share/php5/PEAR/Math", "Math*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/Math_Stats", "docs/*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/Math_Stats", "tests/*")
