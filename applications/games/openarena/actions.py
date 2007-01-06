#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir = "."

def setup():
    shelltools.system("bunzip2 source/ioq3sources.tar.bz2")
    shelltools.system("tar -xvf source/ioq3sources.tar")

def build():
    shelltools.cd("ioq3-svn982")
    autotools.make()

def install():
    pisitools.insinto("/usr/share/OpenArena", "ioq3-svn982/build/release-linux-i386/*.i386")
    pisitools.dosym("/usr/share/OpenArena/ioquake3.i386", "/usr/bin/openarena")

    pisitools.insinto("/usr/share/OpenArena/baseoa", "baseoa/*")

    pisitools.insinto("/usr/share/pixmaps", "ioq3-svn982/code/unix/quake3.png", "openarena.png")

    pisitools.dodoc("CHANGES", "COPYING", "CREDITS", "LINUXNOTES")
    shelltools.cd("ioq3-svn982")
    pisitools.dodoc("BUGS", "ChangeLog", "NOTTODO", "TODO", "README", "*.txt", "code/unix/LinuxSupport/*")
