#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actisonapi import shelltools

WorkDir="File_Find-1.3.0"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/File","Find.php")
    shelltools.chmod("%s/usr/share/php5/PEAR/File/Find.php" % get.installDIR())
    pisitools.insinto("/usr/share/php5/PEAR/tests/File_Find","tests/*")