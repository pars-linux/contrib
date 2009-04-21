import re
import os
import shutil

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    if not os.path.exists("/var/db/tekir/tekirDB.log"):
        shutil.copyfile("/usr/share/tekir/tekirDB.log", "/var/db/tekir/tekirDB.log")


