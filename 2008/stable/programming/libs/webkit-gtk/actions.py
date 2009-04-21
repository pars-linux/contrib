#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "WebKit-%s" % get.srcVERSION().replace('0.0_', 'r')

def setup():
    shelltools.system("sh autogen.sh --prefix=/usr \
                                     --with-font-backend=freetype \
                                     --enable-video \
                                     --enable-jit")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dodoc("WebKit/LICENSE", "WebCore/LICENSE-*", "SunSpider/TODO", "JavaScriptCore/AUTHORS")
