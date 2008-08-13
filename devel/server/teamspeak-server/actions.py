#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "tss2_rc2"

teamspeak_dir = "/usr/share/teamspeak"

def install():
    for dirs in ("/etc/teamspeak", "/var/lib/teamspeak", "/var/log/teamspeak", "/var/run/teamspeak"):
        pisitools.dodir(dirs)

    for _exe in ["server_linux", "sqlite.so"]:
        pisitools.doexe(_exe, teamspeak_dir)

    pisitools.insinto("%s/sql" % teamspeak_dir, "sqlite_sql/*.sql")
    pisitools.insinto("%s/http" % teamspeak_dir, "httpdocs/*.html")
    pisitools.insinto("%s/http/help" % teamspeak_dir, "httpdocs/help/*.html")
    pisitools.insinto("%s/tcpquerydocs" % teamspeak_dir, "tcpquerydocs/*.txt")

    shelltools.touch("%s/etc/teamspeak/bad_names" % get.installDIR())

    for files in ["httpdocs/gfx/*.jpg", "httpdocs/gfx/*.png", "httpdocs/gfx/*.gif"]:
        pisitools.insinto("%s/http/gfx" % teamspeak_dir, files)

    pisitools.dohtml("manual.html")
    shelltools.copytree("Manual", "%s/usr/share/doc/%s/html/Manual" % (get.installDIR(), get.srcTAG()))
    pisitools.dodoc("changelog.txt", "README")
