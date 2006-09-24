#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

NoStrip = "/"

def setup():
    shelltools.export("WANT_AUTOMAKE", "1.7")
    shelltools.export("WANT_AUTOCONF", "2.5")
    shelltools.system("./autogen.sh")
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

#   Pardus 1.1 Alfa libmpeg3 libquicktime libmpeg3 libquicktime package conflicts
#   Dosya çakışmaları:usr/bin/mpeg3toc from libmpeg3 packageusr/include/quicktime/qtprivate.h frm libquicktime packageusr/bin/mpeg3cat from libmpeg3 packageusr/include/quicktime/quicktime.h from libquicktimepackageusr/bin/mpeg3dump from libmpeg3 package
    pisitools.remove("/usr/bin/mpeg3toc")
    pisitools.remove("/usr/include/quicktime/qtprivate.h")
    pisitools.remove("/usr/bin/mpeg3cat")
    pisitools.remove("/usr/include/quicktime/quicktime.h")
    pisitools.remove("/usr/bin/mpeg3dump")
   
    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "INSTALL", "LICENSE", "NEWS", "TODO", "README.BUILD", "README.cinelerra_rpm", "doc/*")
