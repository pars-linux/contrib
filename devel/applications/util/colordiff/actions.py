#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
    pisitools.dobin("colordiff.pl")
    pisitools.domove("/usr/bin/colordiff.pl", "/usr/bin", "colordiff")

    pisitools.dosed("colordiffrc", "newtext=blue", "newtext=yellow")

    pisitools.insinto("/etc", "colordiffrc")
    pisitools.insinto("/usr/share/doc/%s/examples" % get.srcTAG(), "colordiffrc-lightbg")

    pisitools.doman("colordiff.1")

    pisitools.dodoc("CHANGES", "README*", "COPYING")
