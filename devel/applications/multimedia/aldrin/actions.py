#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import scons

def build():
    pisitools.dosed("SConstruct","{DOC_INSTALL_PATH}/aldrin","{DOC_INSTALL_PATH}/%s" % get.srcTAG())

    scons.make('DESTDIR="%s"\
                PREFIX="/%s"' % (get.installDIR(), get.defaultprefixDIR()))

def install():
    scons.install()
    pisitools.dodoc("CREDITS","LICENCE")
