#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import libtools
from pisi.actionsapi import get

def setup():
    # fix Makefile not to run gnome-font-install
    # works just fine as a patch
    # pisitools.dosed("installer/Makefile.in", "$(PERL) $(top_srcdir)/run-gnome-font-install ./gnome-font-install $(datadir) $(top_srcdir) $(sysconfdir)" ,"echo $(top_srcdir)/run-gnome-font-install ./gnome-font-install $(datadir) $(top_srcdir) $(sysconfdir)")
    
    libtools.libtoolize()
    autotools.configure("enable-nls")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.insinto("/usr/share/fonts", "run-gnome-font-install")
    pisitools.dodoc("ABOUT-NLS", "AUTHORS", "ChangeLog", "COPYING*", "INSTALL", "NEWS", "README", "TODO")
