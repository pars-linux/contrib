#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="confuse-%s" % get.srcVERSION()

def setup():
    autotools.configure("--enable-static=no \
                         --enable-shared=yes \
                         --enable-nls \
                         --disable-build-doc")

def build():
    autotools.make()

def install():
    autotools.install()

    # remove empty dir
    pisitools.removeDir("/usr/bin")

    pisitools.dodoc("AUTHORS", "README", "ChangeLog", "TODO", "NEWS")
