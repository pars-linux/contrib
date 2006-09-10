#!/usr/bin/python

import os

def postInstall():
    os.system("texmf-update")

def preRemove():
    os.system("texmf-update")
