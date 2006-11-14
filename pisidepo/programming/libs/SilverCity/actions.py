#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def install():
    pythonmodules.install()

    pisitools.dosed("%s/usr/bin/cgi-styler-form.py" % get.installDIR(), \
                    "#!/usr/home/sweetapp/bin/python", \
                    "#!/usr/bin/env python")

    shelltools.chmod("%s/usr/lib/python2.4/site-packages/SilverCity/default.css" % get.installDIR(), 0644)

    pisitools.dodoc("LICENSE.txt", "README.txt")