#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2005-2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import libtools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    shelltools.export("GST_REGISTRY", "%s/registry.xml" % get.curDIR())

    autotools.configure("--with-nspr-includes=/usr/include/nspr \
                         --with-nspr-libs=/usr/lib/nspr \
                         --with-nss-includes=/usr/include/nss   \
                         --with-nss-libs=/usr/lib/nss \
                         --without-openldap \
                         --enable-ssl \
                         --enable-ipv6 \
                         --enable-gtk-doc")
#--enable-gnome-keyring eklenecek

    shelltools.export("GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL", "")

def build():
    autotools.make()

def install():
    shelltools.export("GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL", "1")

    autotools.install("scrollkeeper_localstate_dir=%s/var/lib/scrollkeeper" % get.installDIR())

    shelltools.export("GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL", "")

    pisitools.remove("/usr/share/applications/mimeinfo.cache")
