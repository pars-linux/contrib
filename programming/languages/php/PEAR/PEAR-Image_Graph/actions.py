#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="Image_Graph-0.7.2"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/Image", "Graph*")
    pisitools.insinto("/usr/share/php5/PEAR/doc/Image_Graph", "docs/*")
    pisitools.insinto("/usr/share/php5/PEAR/tests/Image_Graph", "tests/*")