#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2008 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import get
from pisi.actionsapi import pisitools

WorkDir="Gtk2-%s" % get.srcVERSION()
examples = "%s/%s/examples" % (get.docDIR(), get.srcNAME())
demo = "%s/%s/demo" % (get.docDIR(), get.srcNAME())

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def install():
    perlmodules.install()

    pisitools.insinto(examples, "examples/*")
    pisitools.insinto(demo, "gtk-demo/*")
    pisitools.remove("/usr/lib/perl5/vendor_perl/%s/i686-linux-thread-multi/auto/Gtk2/.packlist" % get.curPERL())

    pisitools.dodoc("AUTHORS", "NEWS", "MAINTAINERS", "README", "TODO")
