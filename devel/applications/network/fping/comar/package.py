#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.chmod("/usr/sbin/fping", 04755)
