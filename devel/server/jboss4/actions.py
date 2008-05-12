#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = 'jboss-%s.GA-src' % get.srcVERSION()

INSTALL_DIR = '/opt/jboss4'
PKG_SRC = 'build/output/jboss-%s.GA' % get.srcVERSION()

BIN_FILES = ('jboss_init_suse.sh',
             'jboss_init_redhat.sh',
             'jboss_init_hpux.sh',
             '*.bat',)

DIRS = ('server',
        'client',
        'lib',
        'bin')

def build():
    shelltools.cd("build")
    shelltools.system("sh build.sh -Dgroups=all")

def install():
    pisitools.dodir(INSTALL_DIR)

    for directory in DIRS:
        pisitools.insinto(INSTALL_DIR, "%s/%s" % (PKG_SRC,directory))

    for f in BIN_FILES:
        pisitools.remove('%s/bin/%s' % (INSTALL_DIR, f))

    pisitools.dodir("/var/log/jboss4")
    pisitools.dosym("/var/log/jboss4", "%s/server/default/log" % INSTALL_DIR)

    pisitools.insinto("/usr/share/doc/%s/" % get.srcTAG(), "%s/docs/*" % PKG_SRC)
