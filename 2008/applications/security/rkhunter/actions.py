#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

def setup():
    pisitools.dosed("files/rkhunter.conf", "/usr/local","/usr")
    pisitools.dosed("files/rkhunter.conf", "#DBDIR=/var/lib/rkhunter/db","DBDIR=/var/lib/rkhunter/db\nINSTALLDIR=/var")
    pisitools.dosed("files/rkhunter.conf", "#TMPDIR=/var/lib/rkhunter/tmp","TMPDIR=/var/lib/rkhunter/tmp")
    pisitools.dosed("files/rkhunter.conf", "#SCRIPTDIR=/usr/lib/rkhunter/scripts","SCRIPTDIR=/var/lib/rkhunter/scripts")

def install():
    pisitools.insinto("/var/lib/rkhunter/db","files/*.dat")
    pisitools.insinto("/var/lib/rkhunter/db/i18n","files/i18n/*")
    pisitools.insinto("/etc","files/rkhunter.conf")
    pisitools.doexe("files/*.pl", "/var/lib/rkhunter/scripts")
    pisitools.doexe("files/check_update.sh", "/var/lib/rkhunter/scripts")
    pisitools.dodir("/var/lib/rkhunter/tmp")
    pisitools.dobin("files/rkhunter")
    pisitools.doman("files/rkhunter.8")
    pisitools.dodoc("files/CHANGELOG", "files/LICENSE", "files/README", "files/WISHLIST")
