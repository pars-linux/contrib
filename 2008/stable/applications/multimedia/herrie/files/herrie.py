#!/usr/bin/python
# -*- coding: utf-8 -*-

# A wrapper script for herrie. Herrie automatically saves playlists to ~/.herrie/playlist.xspf but ~/.herrie 
# doesn't exist by default and herrie doesn't create that directory. Control whether ~/.herrie exits and create it if doesn't exist

# Also, start pulseaudio if it isn't running. On Pardus 2008, pulseaudio is default and ALSA libs use it.

import os
import subprocess
import sys

HERRIE_DIR = "%s/.herrie" % os.environ['HOME']
PULSE_DIR = "/tmp/pulse-%s/pid" % os.environ['USER']

if not os.path.exists(HERRIE_DIR):
    os.mkdir(HERRIE_DIR, 0744)

if not os.path.exists(PULSE_DIR):
    subprocess.call(["pulseaudio", "-D"])

args = " ".join(sys.argv[1:])
subprocess.call(["/usr/bin/herrie-bin", args])
