#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure("--disable-schemas-install \
                         --enable-python \
                         --enable-python-plugins")

def build():
    autotools.make("-j1")

def install():
    autotools.install()

    mimeFiles = ["/usr/share/mime/XMLnamespaces",
                 "/usr/share/mime/aliases",
                 "/usr/share/mime/globs",
                 "/usr/share/mime/magic",
                 "/usr/share/mime/mime.cache",
                 "/usr/share/mime/subclasses"]

    for file in mimeFiles:
        pisitools.remove(file)

    pisitools.dodoc("AUTHORS", "Changelog", "NEWS", "README", "COPYING")
