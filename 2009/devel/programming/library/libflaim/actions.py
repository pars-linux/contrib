#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005-2010 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import autotools
from pisi.actionsapi import get

def build():
    autotools.make("OSTYPE=linux HOSTTYPE=x86")

def install():
    autotools.rawInstall("rpm_build_root=%s OSTYPE=linux HOSTTYPE=x86" % get.installDIR())

    pisitools.dohtml("docs/docs/html/*")
