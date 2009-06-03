#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("ruby setup.rb config")

def build():
    shelltools.system("ruby setup.rb setup")

def install():
    shelltools.system("ruby setup.rb install --prefix=%s" % get.installDIR())

    pisitools.insinto("%s/%s/html" % (get.docDIR(), get.srcTAG()), "doc/faq/*")
    pisitools.insinto("%s/%s/html" % (get.docDIR(), get.srcTAG()), "api" )

    pisitools.dodoc("ChangeLog", "README")
