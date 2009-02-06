#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

os.environ['GCONF_CONFIG_SOURCE'] = "xml:merged:/etc/gconf/gconf.xml.defaults"

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system('update-mime-database /usr/share/mime')
    os.system('gconftool-2 --makefile-install-rule /etc/gconf/schemas/comicbook.schemas')

def preRemove():
    os.system('gconftool-2 --makefile-uninstall-rule /etc/gconf/schemas/comicbook.schemas')
