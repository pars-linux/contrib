import os

def postInstall():
    os.system("/usr/bin/install-catalog --add /etc/sgml/xml-docbook-4.2.cat /usr/share/sgml/docbook/xml-dtd-4.2/docbook.cat")
    os.system("/usr/bin/build-docbook-catalog")
