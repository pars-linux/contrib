#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.install()

    # ignore error Tip of the Day
    pisitools.rename("/usr/share/fityk/tips.txt", "fityk_tips.txt")

    # don't need header
    pisitools.removeDir("/usr/include")

    pisitools.insinto("/usr/share/doc/%s/html" % get.srcTAG(), "doc/fitykhelp_img")

    pisitools.dohtml("doc/fitykhelp.html", "doc/html.css")
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "README", "TODO", "NEWS")
