#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Serkan Avcı <killer@wolke7.net>

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get
import os
from os.path import join

WorkDir1="loosecannon-0.5.0/share/loosecannon"

def setup():
#	    pisitools.dosed("configure", '^#define DATADIR.*','#define DATADIR "/usr/share"')
#    autotools.configure()
 shelltools.system("./configure --prefix=/usr --host=i686-pc-linux-gnu --mandir=/usr/share/man --infodir=/usr/share/info --localstatedir=/usr/lib")

def build():
    autotools.make()

def install():
#	    autotools.install()
	    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
	    pisitools.dodir("/usr/share")
	    shelltools.cd("../")
	    shelltools.copytree(WorkDir1, "%s/usr/share/loosecannon" % get.installDIR())