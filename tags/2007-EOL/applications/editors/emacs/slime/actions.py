#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import pisitools

def install():
    for data in ['*.lisp', '*.el']:
        pisitools.insinto('/usr/share/emacs/site-lisp/slime/', data)
