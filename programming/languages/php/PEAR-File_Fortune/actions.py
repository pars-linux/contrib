#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir="File_Fortune-0.9.0"

def install():
    shelltools.cd("File")
    pisitools.insinto("/usr/share/php5/PEAR/File", "Fortune*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/File_Fortune", "tutorials/File_Fortune/*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/File_Fortune", "tests/*")