#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import system as run

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    run("gtk-update-icon-cache -q -t -f /usr/share/icons/hicolor")
