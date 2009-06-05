#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import system as run

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    run("update-desktop-database -q")

def preRemove():
    run("update-desktop-database -q")
