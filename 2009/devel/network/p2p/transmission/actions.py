#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

import glob
import os

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get


def setup():
    autotools.configure("--disable-static \
                         --enable-gtk \
                         --enable-cli \
                         --enable-libnotify \
                         --enable-daemon")

    # For daemon config files.
    pisitools.dodir("/etc/transmission-daemon")


def build():
    autotools.make()

    shelltools.cd("qt/")
    shelltools.system("qmake-qt4 qtr.pro")
    autotools.make()


def install():
    autotools.install()

    pisitools.dodoc("COPYING", "AUTHORS", "README", "ChangeLog", "NEWS")

    ## install transmission-web manually. it's giving an error in 1.92.
    web_dir = '%s/usr/share/%s/web' % (get.installDIR(), get.srcNAME())
    web_subdirs = ['images', 'javascript', 'stylesheets']

    def _remove_unrequired_files(dir_path):
        unrequired_files = glob.glob(os.path.join(dir_path, 'Makefile*'))

        for unrequired_file in unrequired_files:
            shelltools.unlink(unrequired_file)

    # copy
    shelltools.copytree('web/', web_dir)

    # remove unrequired files
    _remove_unrequired_files(web_dir)
    shelltools.unlink(os.path.join(web_dir, 'LICENSE'))
    for root, dirs, files in os.walk(web_dir):
        for name in dirs:
            _remove_unrequired_files(os.path.join(root, name))

    ## and install transmission-qt..
    shelltools.cd("qt/")
    autotools.rawInstall("INSTALL_ROOT=%s/usr" % get.installDIR())
    pisitools.dosym("/usr/bin/qtr", "/usr/bin/transmission-qt")

    pisitools.insinto("%s/%s" % (get.docDIR(), get.srcNAME()),
                       "README.txt", "README-QT")

    pisitools.remove("/usr/share/icons/hicolor/icon-theme.cache")
