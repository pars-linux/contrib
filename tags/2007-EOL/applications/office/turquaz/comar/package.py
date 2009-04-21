#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright © 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

import os

def postInstall():
    os.system("chmod 777 -R /opt/TurquazLinux08Beta5/database")
