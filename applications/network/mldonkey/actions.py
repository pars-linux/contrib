#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    autotools.configure("--disable-multinet \
                         --enable-gui=newgui2 \
                         --enable-opennap \
                         --enable-gnutella \
                         --enable-gnutella2 \
                         --enable-fasttrack \
                         --enable-directconnect \
                         --enable-soulseek \
                         --enable-bittorrent \
                         --enable-filetp \
                         --enable-donkey")

def build():
    autotools.make()

def install():
    autotools.install()

    #ekstra programlar icin
    autotools.make("utils")

    #Mozilla & Firefox plugins
#    pisitools.insinto("/usr/lib/mozilla/plugins", "distrib/ed2k_mozilla/mldonkey_protocol_handler-1.7.xpi")
#    pisitools.insinto("/usr/lib/MozillaFirefox/plugins", "distrib/ed2k_mozilla/mldonkey_protocol_handler-1.7.xpi")
#    pisitools.insinto("/usr/lib/nsbrowser/plugins", "distrib/ed2k_mozilla/mldonkey_protocol_handler-1.7.xpi")
#    pisitools.insinto("/opt/netscape/plugins", "distrib/ed2k_mozilla/mldonkey_protocol_handler-1.7.xpi")


    pisitools.insinto("/usr/lib/mozilla/plugins", "distrib/ed2k_mozilla/mldonkey_protocol_handler-1.7.xpi")
    pisitools.dosym("/usr/lib/mozilla/plugins/mldonkey_protocol_handler-1.7.xpi", "/usr/lib/MozillaFirefox/plugins/mldonkey_protocol_handler-1.7.xpi")
    pisitools.dosym("/usr/lib/mozilla/plugins/mldonkey_protocol_handler-1.7.xpi", "/usr/lib/nsbrowser/plugins/mldonkey_protocol_handler-1.7.xpi")
    pisitools.dosym("/usr/lib/mozilla/plugins/mldonkey_protocol_handler-1.7.xpi", "/opt/netscape/plugins/mldonkey_protocol_handler-1.7.xpi")

#   pisitools.insinto("%s/share/services/" % get.kdeDIR(), "distrib/ed2k_submit/ed2k.protocol") kmldonkey has same file


    #bins
    pisitools.dobin("distrib/ed2k_submit/mldonkey_submit")
    pisitools.dobin("mld_hash")
    pisitools.dobin("make_torrent")
    pisitools.dobin("get_range")
    pisitools.dobin("subconv")
    pisitools.dobin("mlguistarter")
    pisitools.dobin("dp500")
    pisitools.dobin("copysource")
    pisitools.dobin("mlchat")
    pisitools.dobin("svg_converter")
    pisitools.dobin("distrib/kill_mldonkey")
    pisitools.dobin("distrib/mldonkey_command")
    pisitools.dobin("distrib/mldonkey_previewer")
    pisitools.dobin("distrib/make_buginfo")

    #pisitools.insinto("/etc/config", "packages/rpm/mldonkey.init"  mldonkey.sh /etc/sysconfig/mldonkey

    #Daemon olmasi icin gerekirse distrib/ed2k_submit/ altindaki readme dosyasian bakilabilir.
    pisitools.insinto("/etc/init.d/", "distrib/ed2k_submit/mldonkey")

    #mlgui iconu beyenilmezse buda kullanilabilinir. "packages/rpm/mldonkey-icon-X.png", yada "packages/windows/mld.ico"  "packages/windows/mldonkey.bmp"
    #"config/mldonkey.ico"

    #pisitools.insinto("/usr/share/pixmaps/", "packages/rpm/mldonkey-icon-32.png", "mlgui.png")

    pisitools.insinto("/usr/share/icons", "icons/*")
    pisitools.dodoc("docs/*","docs/developers/*", "docs/images/*", "distrib/*.txt", "distrib/FAQ.html", "distrib/ChangeLog")
