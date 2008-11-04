#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):

    if os.path.exists("/opt/netscape/plugins/libflashplayer.so"):
        # Create a symlink in /usr/lib/opera
        os.symlink("/opt/netscape/plugins/libflashplayer.so", "/usr/lib/opera/plugins/libflashplayer.so")

def preRemove():

    if os.path.exists("/usr/lib/opera/plugins/libflashplayer.so"):
        os.unlink("/usr/lib/opera/plugins/libflashplayer.so")
