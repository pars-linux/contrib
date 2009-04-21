#!/usr/bin/python
# -*- coding: utf-8 -*-

# A wrapper script for herrie. Herrie automatically saves playlists to ~/.herrie/playlist.xspf but ~/.herrie 
# doesn't exist by default and herrie doesn't create that directory. Control whether ~/.herrie exits and create it if doesn't exist

import os
import subprocess
import sys

HERRIE_DIR = "%s/.herrie" % os.environ['HOME']

if not os.path.exists(HERRIE_DIR):
    os.mkdir(HERRIE_DIR, 0744)

args = " ".join(sys.argv[1:])
subprocess.call(["/usr/bin/herrie-bin", args])
