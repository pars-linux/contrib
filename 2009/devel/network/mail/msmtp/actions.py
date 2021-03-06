#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-ssl --with-ssl=gnutls")

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.insinto("/usr/share/doc/%s/examples"% get.srcTAG(), "doc/*.example")
    pisitools.insinto("/usr/share/doc/%s/examples"% get.srcTAG(), "scripts/msmtpqueue/*")

    pisitools.dohtml("doc/msmtp.html")
    pisitools.dodoc("AUTHORS", "ChangeLog", "NEWS", "README", "THANKS", "doc/msmtp.pdf", "doc/Mutt+msmtp.txt")
