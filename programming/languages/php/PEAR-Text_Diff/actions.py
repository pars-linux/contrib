#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import shelltools

WorkDir="Text_Diff-0.2.1"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/Text", "Diff*")
    # i don't know why chmod of string.php is not readable for users instead of root?
    shelltools.chmod("%s/usr/share/php5/PEAR/Text/Diff/Engine/string.php" % get.installDIR())
    pisitools.insinto("/usr/share/php5/PEAR/doc/Text_Diff", "docs/*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/Text_Diff", "tests/*")