#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="Amaya%s" % get.srcVERSION()

def setup():
    # Create a subdirectory for your Pardus
    shelltools.makedirs("%s/Amaya%s/Amaya/Pardus" % (get.workDIR(), get.srcVERSION()))
    shelltools.cd("%s/Amaya%s/Amaya/Pardus" % (get.workDIR(), get.srcVERSION()))

    shelltools.system("ln -s ../configure")
    autotools.configure("--prefix=/usr \
                         --with-wx \
                         --with-mesa \
                         --without-gtk \
                         --enable-svg \
                         --enable-generic-xml \
                         --with-graphiclibs")

def build():
    shelltools.cd("%s/Amaya%s/Amaya/Pardus" % (get.workDIR(), get.srcVERSION()))
    autotools.make()

def install():
    shelltools.cd("%s/Amaya%s/Amaya/Pardus" % (get.workDIR(), get.srcVERSION()))
    pisitools.dodir("/usr/share")

    # run the scripts to install the files to the installation dir
    shelltools.system("./script_install %s/Amaya%s/Amaya/Pardus/bin %s/usr/share" % (get.workDIR(), get.srcVERSION(), get.installDIR()))
    shelltools.system("./script_install_gnomekde %s/Amaya%s/Amaya/Pardus/bin %s/usr/share" % (get.workDIR(), get.srcVERSION(), get.installDIR()))

    # make symbolic link for executable files
    pisitools.dosym("/usr/share/Amaya-%s/wx/bin/amaya" % get.srcVERSION(), "/usr/bin/amaya")
    pisitools.dosym("/usr/share/Amaya-%s/wx/bin/print" % get.srcVERSION(), "/usr/bin/print")

    # remove redundant dirs and files
    pisitools.removeDir("/usr/share/bin")
