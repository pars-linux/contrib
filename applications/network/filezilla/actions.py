#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-static=no \
                         --with-wx-config=/usr/bin/wx-config-2.8 \
                         --with-wx-prefix=/usr/wx/2.8")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    # move fzdefaults.xml.example to /usr/share/filezilla
    pisitools.domove("/usr/share/filezilla/docs/fzdefaults.xml.example", "/usr/share/filezilla")
    pisitools.removeDir("/usr/share/filezilla/docs")

    pisitools.dodoc("ChangeLog", "README", "AUTHORS", "docs/todo.txt")

