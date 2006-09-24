#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.


from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get


def setup():
    pass

def build():
    pass

def install():
    autotools.install("BINDIR=%s/usr/bin \
                       DESTDIR=%s/usr/share/sgml/docbook/dsssl-stylesheets-%s" % (get.installDIR(), get.installDIR(), get.srcVERSION()))

    pisitools.dodir("/usr/share/sgml/stylesheets/dsssl")
    pisitools.dosym("/usr/share/sgml/docbook/dsssl-stylesheets-%s" % get.srcVERSION(), "/usr/share/sgml/stylesheets/dsssl/docbook")
    pisitools.dodoc("BUGS", "ChangeLog", "README", "RELEASE-NOTES.txt", "WhatsNew")
