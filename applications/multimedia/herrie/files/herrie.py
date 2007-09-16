#!/usr/bin/python
# -*- coding: utf-8 -*-

# A wrapper script for herrie. Herrie automatically saves playlists to ~/.herrie/playlist.xspf but ~/.herrie 
# doesn't exist by default and it can't make it. Control whether ~/.herrie exits and create it if doesn't exist

import os

HERRIE_DIR = "%s/.herrie" % os.environ['HOME']

if not os.path.exists(HERRIE_DIR):
    os.mkdir(HERRIE_DIR, 0755)

os.system("/usr/bin/herrie-bin")
