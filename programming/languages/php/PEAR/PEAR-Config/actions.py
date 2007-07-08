#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="Config-%s" % get.srcVERSION()

def install():
    pisitools.insinto("/usr/share/php5/PEAR", "Config*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/Config", "test/*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/Config", "docs/*")
