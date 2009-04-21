#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "%s-%s" % (get.srcNAME()[5:], get.srcVERSION())
examples = "%s/%s/examples" % (get.docDIR(), get.srcTAG())

def setup():
    perlmodules.configure()
    shelltools.chmod("examples/*", 0644)

def build():
    perlmodules.make()

def install():
    perlmodules.install()

    pisitools.removeDir("/usr/lib/perl5/5.10.0/")
    pisitools.insinto(examples, "examples/*")
    pisitools.dodoc("ChangeLog", "README")
