#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="Amaya"

def setup():
    shelltools.makedirs("%s/Amaya/Pardus" % get.workDIR())
    shelltools.cd("%s/Amaya/Pardus" % get.workDIR())

    shelltools.system("ln -s ../configure")
    autotools.configure("--prefix=/usr")

def build():
    shelltools.cd("%s/Amaya/Pardus" % get.workDIR())
    autotools.make()

def install():
    shelltools.cd("%s/Amaya/Pardus" % get.workDIR())

    pisitools.dodir("/usr/share")

    # run the scripts to install the files to the installation dir
    shelltools.system("./script_install %s/Amaya/Pardus/bin %s/usr/share" % (get.workDIR(), get.installDIR()))
    shelltools.system("./script_install_gnomekde %s/Amaya/Pardus/bin %s/usr/share" % (get.workDIR(), get.installDIR()))

    # make symbolic link for executable files
    pisitools.dosym("/usr/share/Amaya-9.52/wx/bin/amaya", "/usr/bin/amaya")
    pisitools.dosym("/usr/share/Amaya-9.52/wx/bin/print", "/usr/bin/print")

    # remove redundant dirs and files
    pisitools.removeDir("/usr/share/bin")
