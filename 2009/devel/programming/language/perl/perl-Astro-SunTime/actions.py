#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "Astro-SunTime-%s" % get.srcVERSION()

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def install():
    perlmodules.install()

    pisitools.removeDir("/usr/lib/perl5/5.10.0")
    pisitools.removeDir("/usr/lib/perl5/vendor_perl/%s/i686-linux-thread-multi" % get.curPERL())
    pisitools.dodoc("Changes", "README")
