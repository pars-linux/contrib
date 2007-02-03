import os

def postInstall():
    os.system("find  /etc/gconf/ -type d -exec chmod ugo+rx "{}" \;")
    os.system("find  /etc/gconf/ -type f -exec chmod ugo+r "{}" \;")

def preRemove():
    os.system("echo 'CONFIG_PROTECT_MASK="/etc/gconf"' > ${IMAGE}/etc/env.d/50gconf")