#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "ts2_client_rc2_2032/setup.data/image"

teamspeak_dir = "/usr/share/teamspeak"

def setup():
    pisitools.dosed("TeamSpeak", "%installdir%", teamspeak_dir)

def install():
    pisitools.dobin("TeamSpeak")
    pisitools.rename("/usr/bin/TeamSpeak", "teamspeak-client")

    for _exe in ["TeamSpeak.bin", "libborqt-6.9-qt2.3.so", "libHVDI.so.0.8.0", "libspeex.so.1.0.0"]:
        pisitools.doexe(_exe, teamspeak_dir)

    for _exe in ["client_sdk/tsControl", "client_sdk/libTSRemote.so.0.4"]:
        pisitools.doexe(_exe, "%s/client_sdk" % teamspeak_dir)

    for files in ["client_sdk/tsControl.dpr", "client_sdk/TsRemoteImport.pas"]:
        pisitools.insinto("%s/client_sdk" % teamspeak_dir, files)

    pisitools.insinto("%s/sounds" % teamspeak_dir, "sounds/*")

    pisitools.insinto("/usr/share/doc/%s/html/manual" % get.srcTAG(), "manual/*")
    pisitools.dosym("/usr/share/doc/%s/html/manual" % get.srcTAG(), "%s/manual" % teamspeak_dir)

    pisitools.dodoc("*.txt", "client_sdk/*.txt")
