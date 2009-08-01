#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir = "%s-%s" % (get.srcNAME()[5:], get.srcVERSION())

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def install():
    perlmodules.install()

    pisitools.removeDir("/usr/lib/perl5/%s" % get.curPERL())
    pisitools.remove("/usr/lib/perl5/vendor_perl/%s/i686-linux-thread-multi/auto/Gtk2/TrayIcon/.packlist" % get.curPERL())
    pisitools.dodoc("TODO", "ChangeLog", "README")
