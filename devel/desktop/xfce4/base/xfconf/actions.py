#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure("--disable-static \
                         --enable-perl-bindings")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # change modes
    shelltools.chmod("%s/usr/lib/perl5/site_perl/%s/i686-linux-thread-multi/Xfce4/*.pm" % (get.installDIR(), get.curPERL()), 0644)
    shelltools.chmod("%s/usr/lib/perl5/site_perl/%s/i686-linux-thread-multi/Xfce4/Xfconf/Install/*" % (get.installDIR(), get.curPERL()), 0644)
    shelltools.chmod("%s/usr/lib/perl5/site_perl/%s/i686-linux-thread-multi/auto/Xfce4/Xfconf/*" % (get.installDIR(), get.curPERL()), 0644)

    # and add docs
    pisitools.dodoc("NEWS", "README", "COPYING", "TODO", "ChangeLog", "AUTHORS")
