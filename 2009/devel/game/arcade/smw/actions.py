#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006-2010  TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "smw1.7afe"

def setup():
    shelltools.chmod(get.workDIR() + "/smw1.7afe/configure", 0755)
    autotools.configure()

def build():
    autotools.make()

def install():
    # veri dosyalarını kurduramadım
    # insinto veya copytree ile bir şeyler yapılabilir
    # ayrıca dosya izinlerinin de değişmesi gerekiyor
    # yoksa ancak sudo smw
    # autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dobin("smw")
    pisitools.dobin("leveledit")

    pisitools.dohtml("README.html")
    pisitools.dodoc("WHATSNEW.txt", "README.txt")
