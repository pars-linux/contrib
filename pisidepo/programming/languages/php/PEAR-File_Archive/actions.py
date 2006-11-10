#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="File_Archive-1.5.3"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/File", "File/Archive.php")
    pisitools.insinto("/usr/share/php5/PEAR/File/Archive", "File/Archive/*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/File_Archive", "File/doc/*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/File_Archive", "File/tests/*")