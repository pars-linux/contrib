#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import perlmodules

def setup():
    perlmodules.configure()

def build():
    perlmodules.make()

def install():
    perlmodules.install()

    pisitools.removeDir("/usr/lib/perl5/5.10.0/")
    pisitools.dodoc("ack-help*.txt", "README", "Changes", "TODO")
