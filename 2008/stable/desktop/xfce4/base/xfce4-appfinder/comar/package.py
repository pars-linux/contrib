#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system("update-desktop-database -q")
    os.system("gtk-update-icon-cache -q -t -f /usr/share/icons/hicolor")

def postRemove(fromVersion, fromRelease, toVersion, toRelease):
    os.system("update-desktop-database -q")
    os.system("gtk-update-icon-cache -q -t -f /usr/share/icons/hicolor")
