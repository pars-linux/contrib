#!/usr/bin/python
# -*- coding: utf-8 -*-

import piksemel
import os

def updateScrollkeeperDatabase(filepath):
    parse = piksemel.parse(filepath)
    for omf in parse.tags("File"):
        path = omf.getTagData("Path")
        if path.startswith("usr/share/omf"):
            os.system("/usr/bin/scrollkeeper-update -p /var/scrollkeeper -o /usr/share/omf")

def setupPackage(metapath, filepath):
    updateScrollkeeperDatabase(filepath)

def cleanupPackage(metapath, filepath):
    updateScrollkeeperDatabase(filepath)
