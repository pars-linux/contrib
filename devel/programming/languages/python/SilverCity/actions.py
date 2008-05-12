#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    pythonmodules.install()

    pisitools.dosed("%s/usr/bin/cgi-styler-form.py" % get.installDIR(), "home/sweetapp/")

    pisitools.chmod("%s/usr/lib/%s/site-packages/SilverCity/default.css" % (get.installDIR(), get.curPYTHON()), 0644)

    pisitools.dodoc("LICENSE.txt", "README.txt")