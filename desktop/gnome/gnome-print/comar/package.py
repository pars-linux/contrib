import os

def postInstall():
    os.system("ldconfig >/dev/null 2>/dev/null")
    os.system("perl /usr/share/fonts/run-gnome-font-install \
              /usr/bin/gnome-font-install \
              /usr/share/fonts /usr/share/fonts /etc >/dev/null 2>/dev/null")
