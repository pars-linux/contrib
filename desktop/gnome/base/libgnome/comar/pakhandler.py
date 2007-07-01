#!/usr/bin/python
# -*- coding: utf-8 -*-

import piksemel
import os

def installGconfSchemas(filepath):
    os.environ['GCONF_CONFIG_SOURCE'] = 'xml:merged:/etc/gconf/gconf.xml.defaults'
    parse = piksemel.parse(filepath)
    for schema in parse.tags("File"):
        path = schema.getTagData("Path")
        if path.startswith("etc/gconf/schemas"):
            os.system("/usr/bin/gconftool-2 --makefile-install-rule /%s" % path)

def uninstallGconfSchemas(filepath):
    os.environ['GCONF_CONFIG_SOURCE'] = 'xml:merged:/etc/gconf/gconf.xml.defaults'
    parse = piksemel.parse(filepath)
    for schema in parse.tags("File"):
        path = schema.getTagData("Path")
        if path.startswith("etc/gconf/schemas"):
            os.system("/usr/bin/gconftool-2 --makefile-uninstall-rule /%s" % path)

def updateIconCache(filepath):
    parse = piksemel.parse(filepath)
    for icon in parse.tags("File"):
        path = icon.getTagData("Path")
        if path.startswith("usr/share/icons/hicolor"):
            os.system("/usr/bin/gtk-update-icon-cache -f /usr/share/icons/hicolor")

def updateScrollkeeperDatabase(filepath):
    parse = piksemel.parse(filepath)
    for omf in parse.tags("File"):
        path = omf.getTagData("Path")
        if path.startswith("usr/share/omf"):
            os.system("/usr/bin/scrollkeeper-update -p /var/scrollkeeper -o /usr/share/omf")

def setupPackage(metapath, filepath):
    installGconfSchemas(filepath)
    updateScrollkeeperDatabase(filepath)
    updateIconCache(filepath)

def cleanupPackage(metapath, filepath):
    uninstallGconfSchemas(filepath)
    updateScrollkeeperDatabase(filepath)
    updateIconCache(filepath)
