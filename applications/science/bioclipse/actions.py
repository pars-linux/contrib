#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "Bioclipse"
directory = "/opt/Bioclipse"

def install():
    pisitools.dodir(directory)

    for i in ["about_files", "configuration", "features", "plugins", "workspace"]:
        shelltools.copy(i, "%s/%s" % (get.installDIR(), directory))

    for files in ["Bioclipse.ini", "startup.jar"]:
        pisitools.insinto(directory, files)

    for exes in ["Bioclipse", "libcairo-swt.so"]:
        pisitools.doexe(exes, directory)

    pisitools.dohtml("about.html")
