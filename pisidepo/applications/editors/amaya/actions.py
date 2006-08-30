#!/usr/bin/python
# -*- coding: utf-8 -*-
#Murat Şenel <> muratasenel at gmail.com <>

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="Amaya"

def setup():
    shelltools.makedirs("%s/Amaya/obj" % get.workDIR())
    shelltools.cd("%s/Amaya/obj" % get.workDIR())
    shelltools.system("ln -s ../configure")
    autotools.configure("--prefix=/usr/share")

def build():
    shelltools.cd("%s/Amaya/obj" % get.workDIR())
    autotools.make()

def install():
    shelltools.cd("%s/Amaya/obj" % get.workDIR())

    pisitools.dodir("/usr/share")

    #run the scripts to install the files to the installation dir
    shelltools.system("./script_install %s/Amaya/obj/bin %s/usr/share" % (get.workDIR(), get.installDIR()))
    shelltools.system("./script_install_gnomekde %s/Amaya/obj/bin %s/usr/share" % (get.workDIR(), get.installDIR()))

    #make symbolic link for executable files
    pisitools.dosym("/usr/share/Amaya-9.51/wx/bin/amaya", "/usr/bin/amaya")
    pisitools.dosym("/usr/share/Amaya-9.51/wx/bin/print", "/usr/bin/print")

    pisitools.domove("/usr/share/Amaya-9.51/doc/*", "/usr/share/doc/%s" % get.srcTAG())

    #Turkish supoort activated
    pisitools.dosed("%s/usr/share/Amaya-9.51/config/unix-thot.rc" % get.installDIR(), "LANG=en","LANG=tr")

    #remove redundant dirs and files
    pisitools.removeDir("/usr/share/bin")
    pisitools.removeDir("/usr/share/Amaya-9.51/doc")





