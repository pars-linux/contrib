#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import pythonmodules

def setup():
    autotools.configure("--disable-scrollkeeper \
                         --disable-schemas-install \
                         --disable-mime-install")

def build():
    autotools.make()

def install():
    autotools.install()

    pythonmodules.fixCompiledPy(lookInto="/usr/share/gramps")

    # remove TR locale, it hasn't been translated completely
    pisitools.remove("/usr/share/locale/tr/LC_MESSAGES/gramps.mo")

    mimeFiles = ["/usr/share/mime/XMLnamespaces",
                 "/usr/share/mime/aliases",
                 "/usr/share/mime/globs",
                 "/usr/share/mime/magic",
                 "/usr/share/mime/mime.cache",
                 "/usr/share/mime/subclasses"]

    for file in mimeFiles:
        pisitools.remove(file)

    pisitools.dodoc("AUTHORS", "ChangeLog", "README","NEWS","FAQ","TODO")
