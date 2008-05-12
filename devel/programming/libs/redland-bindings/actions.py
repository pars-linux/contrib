#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import get

def setup():
    shelltools.export("LDFLAGS", "")

    autotools.configure("--with-python \
                         --with-tcl \
                         --with-redland=system \
                         --with-perl \
                         --with-java \
                         --with-php \
                         --with-ruby \
                         --with-jdk")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog*", "COPYING*", "NEWS", "README", "TODO")
    pisitools.dohtml("*.html")

    perlmodules.fixLocalPod()
