#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-shared")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # needed symlink http://bugs.gentoo.org/show_bug.cgi?id=93311
    pisitools.dosym("/usr/lib/itk3.4/libitk3.4.so","/usr/lib/libitk3.4.so")

    pisitools.dodoc("license.terms")
