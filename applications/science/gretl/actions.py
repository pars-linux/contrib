#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.autoconf()

    autotools.configure("--with-readline \
                         --without-gnome \
                         --without-gtksourceview \
                         --enable-png-comments \
                         --enable-build-doc \
                         --with-gmp \
                         --with-mpfr \
                         --without-audio")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dobin("gretl-config")

    pisitools.insinto("/usr/share/applications", "gnome/gretl.desktop")
    pisitools.insinto("/usr/share/pixmaps", "gnome/gretl.png")
    pisitools.insinto("/usr/share/aclocal", "gretl.m4")
    pisitools.insinto("/usr/share/emacs/site-lisp", "utils/emacs/gretl.el")

    pisitools.doman("gretlcli.1")

    pisitools.dodoc("ABOUT-NLS", "ChangeLog", "COPYING", "EXTENDING", "NEWS", "README", "README.audio", "TODO")
