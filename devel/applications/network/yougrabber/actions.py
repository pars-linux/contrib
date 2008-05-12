#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def build():
    shelltools.cd("src")
    shelltools.system("make")
    shelltools.cd("..")

def install():
    pisitools.dobin("src/yg")
    pisitools.doman("man/yg.1")

    # symlinks for better usage, I would first try to use "yougrabber" binary because of the package name :)
    pisitools.dosym("/usr/bin/yg", "/usr/bin/yougrabber")
    pisitools.dosym("/usr/share/man/man1/yg.1", "/usr/share/man/man1/yougrabber.1")

    pisitools.dodoc("doc/LICENSE", "doc/README", "doc/CHANGELOG", "yg.conf.sample")
