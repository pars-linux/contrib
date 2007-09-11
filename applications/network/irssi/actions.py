#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import perlmodules
from pisi.actionsapi import get

WorkDir = "irssi-0.8.12-rc1"

def setup():
    autotools.configure("--enable-ipv6 \
                         --enable-ssl \
                         --disable-glibtest \
                         --with-socks \
                         --with-textui \
                         --with-bot \
                         --with-proxy \
                         --with-terminfo \
                         --with-modules \
                         --without-perl-staticlib")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.remove("/usr/lib/irssi/modules/libirc_proxy.a")

    pisitools.rename("/usr/bin/irssi", "irssi-bin")

    perlmodules.fixLocalPod()