#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    for d in ["/var/lib/mpd", "/var/lib/mpd/playlists", "/var/log/mpd", "/var/run/mpd"]:
        if not os.path.exists(d):
            os.mkdir(d)
            # $ id nobody
            # uid=65534(nobody) gid=65534(nobody) gruplar=65534(nobody)
            os.chown(d, 65534, 65534)

