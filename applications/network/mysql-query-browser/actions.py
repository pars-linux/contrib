#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir='mysql-gui-tools-5.0'
MyDir='/opt/mysql-query-browser'

def install():
    pisitools.dodoc("COPYING")
    pisitools.dobin("mysql-query-browser-bin", "%s/bin" % MyDir)
    shelltools.copytree("lib/", "%s%s/lib/" % (get.installDIR(), MyDir))
    pisitools.insinto("%s/share/mysql-gui" % MyDir, "share/mysql-gui/MySQLIcon_QueryBrowser*")
    pisitools.insinto("%s/share/mysql-gui/query-browser/" % MyDir, "share/mysql-gui/query-browser/*")
    shelltools.copytree("share/mysql-gui/common/", "%s%s/share/mysql-gui/" % (get.installDIR(), MyDir))
