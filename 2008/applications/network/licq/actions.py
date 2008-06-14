#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

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
        # msn, auto-reply, email plugins have deprecated vector.h check, configure.ac has been patched
        # and ./configure should be re-created
        autotools.aclocal()
        autotools.autoconf()
        autotools.configure()

def build():
    autotools.make()

    shelltools.cd("plugins/qt-gui")
    autotools.make()

    # Optional Plugins
    li = ['rms', 'msn', 'osd', 'console', 'auto-reply', 'email']
    for name in li:
        shelltools.cd("../%s" % name)
        autotools.make()

def install():
    autotools.rawInstall('DESTDIR="%s"'  % get.installDIR())

    shelltools.cd("plugins/qt-gui")
    autotools.rawInstall('DESTDIR="%s"'  % get.installDIR())

    # Optional Plugins
    li = ['rms', 'msn', 'osd', 'console', 'auto-reply', 'email']
    for name in li:
        shelltools.cd("../%s" % name)
        autotools.rawInstall('DESTDIR="%s"'  % get.installDIR())

    # Licq-web plugin
    pisitools.dodir("/var/www/localhost/htdocs")
    shelltools.copytree("../licqweb/", "%s/var/www/localhost/htdocs/licqweb/" % get.installDIR())

    pisitools.dodoc("README", "README.GPG", "README.ICS", "README.OPENSSL", "LICENSE", "ChangeLog", "doc/*")
