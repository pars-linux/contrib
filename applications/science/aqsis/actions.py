#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2006-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import scons
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir = "dist_aqsis-1.2.0rc2"

def install():
    shelltools.export("LD_LIBRARY_PATH", "%s/%s/lib" % (get.installDIR(), get.defaultprefixDIR()))
    scons.install("install_prefix=/%s sysconfdir=/%s/aqsis install" % (get.defaultprefixDIR(), get.confDIR()), get.installDIR(), "destdir")

    pisitools.dodoc("AUTHORS", "COPYING", "README", "ReleaseNotes")
