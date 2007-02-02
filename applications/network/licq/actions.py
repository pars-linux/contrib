#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
    autotools.configure()
    shelltools.cd("plugins/qt-gui")
    autotools.configure("--with-kde")

    # Optional Plugins
    li = ['rms', 'msn', 'osd', 'console', 'auto-reply', 'email']
    for name in li:
        shelltools.cd("../%s" % name)
        autotools.configure()

def build():
    autotools.make()

    # Plugins
    shelltools.cd("plugins/qt-gui")
    autotools.make()

    # Optional Plugins
    li = ['rms', 'msn', 'osd', 'console', 'auto-reply', 'email']
    for name in li:
        shelltools.cd("../%s" % name)
        autotools.make()

def install():
    pisitools.dodoc("README", "README.FREEBSD", "README.GPG", "README.ICS", "README.OPENSSL", "LICENSE", "INSTALL", "ChangeLog", "doc/*")
    autotools.install()
    shelltools.cd("plugins/qt-gui")
    autotools.install()

    # Optional Plugins
    li = ['rms', 'msn', 'osd', 'console', 'auto-reply', 'email']
    for name in li:
        shelltools.cd("../%s" % name)
        autotools.install()

    # Licq-web plugin
    pisitools.dodir("/var/www/localhost/htdocs")
    shelltools.copytree("../licqweb/", "%s/var/www/localhost/htdocs/licqweb/" % get.installDIR())
