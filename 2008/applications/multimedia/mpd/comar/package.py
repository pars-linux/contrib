#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    for d in ["/var/lib/mpd", "/var/lib/mpd/playlists", "/var/log/mpd"]:
        if not os.path.exists(d):
            os.mkdir(d)

