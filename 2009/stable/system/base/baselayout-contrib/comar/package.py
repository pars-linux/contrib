#!/usr/bin/python

import os
import grp
import pwd

def hav(method, args):
    try:
        call("baselayout", "User.Manager", method, args)
    except:
        pass

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    # build user -> group map for migration
    def deleteGroup(group):
        try:
            gid = grp.getgrnam(group)[2]
            # deleteGroup(gid)
            hav("deleteGroup", (gid))
        except KeyError:
            pass

    def deleteUser(user):
        try:
            uid = pwd.getpwnam(user)[2]
            # deleteUser(uid, delete_files)
            hav("deleteUser", (uid, False))
        except KeyError:
            pass

    # Remove old groups/users
    groups = ["teamspeak", "gdm"]

    for group in groups:
        deleteGroup(group)

    users = ["teamspeak", "gdm", "mpd"]

    for user in users:
        deleteUser(user)

    # Merge new system groups
    # addGroup(gid, name)
    hav("addGroup", (400, "teamspeak"))
    hav("addGroup", (114, "gdm"))

    # Merge new system users
    # addUser(uid, nick, realname, homedir, shell, password, groups, grantedauths, blockedauths)
    hav("addUser", (400, "teamspeak", "Teamspeak", "/dev/null", "/bin/false", "", ["teamspeak"], [], []))
    hav("addUser", (105, "gdm", "GNOME Display Manager", "/dev/null", "/bin/bash", "", ["gdm"], [], []))
    hav("addUser", (250, "mpd", "Music Player Daemon", "/var/lib/mpd", "/bin/bash", "", ["audio", "pulse", "pulse-access", "pulse-rt"], [], []))

