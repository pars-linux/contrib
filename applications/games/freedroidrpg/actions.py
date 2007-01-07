#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi.libtools import gnuconfig_update
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    gnuconfig_update()

    autotools.configure("--enable-opengl \
                         --disable-editors \
                         --disable-sdltest \
                         --disable-gtktest \
                         --with-x \
                         --with-sdl")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "FILES", "HELP_WANTED", "INSTALL*", "IDEAS", "NEWS", "README")
