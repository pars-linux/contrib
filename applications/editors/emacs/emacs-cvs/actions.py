#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

WorkDir="emacs"

def setup():
    autotools.configure("--with-gtk \
                         --with-xft \
                         --with-freetype \
                         --enable-font-backend \
                         --program-suffix=-unicode")

def build():
    autotools.make("bootstrap")

def install():
    autotools.install()

    # Conflicts with emacs
    pisitools.removeDir("/usr/share/info")
    pisitools.removeDir("/usr/share/man")
    pisitools.removeDir("/var/lib/games/")
    pisitools.remove("/usr/share/emacs/site-lisp/subdirs.el")

    pisitools.dodoc("ChangeLog", "BUGS", "README")
