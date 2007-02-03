import os

def postInstall():
    os.system("/usr/bin/install-catalog --add /etc/sgml/xml-docbook-4.5.cat /usr/share/sgml/docbook/xml-dtd-4.5/docbook.cat")
    os.system("/usr/bin/build-docbook-catalog")
