#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import pisitools

WorkDir="Image_GraphViz-1.3.0RC3"

def install():
    pisitools.insinto("/usr/share/php5/PEAR/Image", "GraphViz.php")
    pisitools.insinto("/usr/share/php5/PEAR/tests/Image_GraphViz", "tests/*")
