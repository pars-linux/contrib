#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-static=no \
                         --disable-qt \
                         --disable-gtk \
                         --disable-wxwidgets")

    # we use only console edition and binary name should be the same with package (weechat-curses -> weechat)
    pisitools.dosed("doc/weechat-curses.1", "weechat-curses", "weechat")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.domove("/usr/bin/weechat-curses", "/usr/bin", "weechat")

    pisitools.domove("/usr/share/man/man1/weechat-curses.1", "/usr/share/man/man1", "weechat.1")

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")
