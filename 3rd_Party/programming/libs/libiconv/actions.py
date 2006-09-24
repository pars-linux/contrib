#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    #XxxxxxxxxxxxxxxxxxxxxX
    #File Conflicts:
    #/usr/lib/libiconv.so from sancho package
    #/usr/lib/libiconv.so.2.2.0 from sancho package
    #/usr/lib/libiconv.so.2 from sancho package
    #i removed it from sancho those files.
    #pisitools.remove("/usr/lib/libiconv.so")
    #pisitools.remove("/usr/lib/libiconv.so.2")
    #pisitools.remove("/usr/lib/libiconv.so.2.2.0")

    #/usr/share/man/man3/iconv.3 from man-pages package
    #/usr/share/man/man3/iconv_open.3 from man-pages package
    #/usr/share/man/man3/iconv_close.3 from man-pages package
    #man-pages conflicts
    pisitools.remove("/usr/share/man/man3/iconv.3")
    pisitools.remove("/usr/share/man/man3/iconv_open.3")
    pisitools.remove("/usr/share/man/man3/iconv_close.3")

    #/usr/bin/iconv from glibc package
    #/usr/include/iconv.h from glibc package
    #glibc conflicts
    pisitools.remove("/usr/bin/iconv")
    pisitools.remove("/usr/include/iconv.h")
    #XxxxxxxxxxxxxxxxxxxxxX

    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING.LIB", "DESIGN", "INSTALL.generic", "NEWS", "NOTES", "PORTS", "README*", "THANKS")
