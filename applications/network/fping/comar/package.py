#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall():
    os.chmod("/usr/sbin/fping", 04755)
