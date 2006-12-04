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
    autotools.configure("--with-dbus \
           		 --with-x \
			 --with-pic \
			 --with-gnu-ld \
			 --enable-ffjs=/usr/lib/MozillaFirefox/libmozjs.so \
			 --disable-mozjs \
			 --disable-libjs")
                         #--without-browser-plugin \ with this option will be no /usr/lib/gxine/ files

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    ###Firefox plugins####  Mplayer plugins are the best of all.
    #pisitools.dosym("/usr/lib/gxine/gxineplugin.so", "/usr/lib/MozillaFirefox/plugins/gxineplugin.so")
    #pisitools.dosym("/usr/lib/gxine/gxineplugin.la", "/usr/lib/MozillaFirefox/plugins/gxineplugin.la")
    #
    #pisitools.dosym("/usr/lib/gxine/gxineplugin.so", "/opt/netscape/plugins/gxineplugin.so")
    #pisitools.dosym("/usr/lib/gxine/gxineplugin.la", "/opt/netscape/plugins/gxineplugin.la")
    #
    #pisitools.dosym("/usr/lib/gxine/gxineplugin.so", "/usr/lib/mozilla/plugins/gxineplugin.so")
    #pisitools.dosym("/usr/lib/gxine/gxineplugin.la", "/usr/lib/mozilla/plugins/gxineplugin.la")
    #
    #pisitools.dosym("/usr/lib/gxine/gxineplugin.so", "/usr/lib/nsbrowser/plugins/gxineplugin.so")
    #pisitools.dosym("/usr/lib/gxine/gxineplugin.la", "/usr/lib/nsbrowser/plugins/gxineplugin.la")
    ###
    
    #with out plugins
    #pisitools.removeDir("/usr/lib")

    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING", "INSTALL", "NEWS", "README*", "TODO")
