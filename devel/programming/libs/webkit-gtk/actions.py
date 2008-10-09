#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

WorkDir = "WebKit-%s" % get.srcVERSION().replace('0.0_', 'r')

def setup():
    libtools.libtoolize("--force")
    autotools.autoreconf("-fi")

    autotools.configure("--with-http-backend=curl \
                         --with-font-backend=pango")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("WebKit/LICENSE", "WebCore/LICENSE-*", "SunSpider/TODO", "JavaScriptCore/AUTHORS")
