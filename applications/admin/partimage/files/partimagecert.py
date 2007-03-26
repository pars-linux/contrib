#!/usr/bin/python

import os

os.system("touch /etc/partimaged/privkey.pem")
os.system("rm -f /etc/partimaged/privkey.pem")
os.system("/usr/bin/openssl req -new -x509 -outform PEM > /etc/partimaged/partimaged.csr")
os.system("/usr/bin/openssl rsa -in privkey.pem -out /etc/partimaged/partimaged.key")
os.system("rm privkey.pem")
os.system("/usr/bin/openssl x509 -in /etc/partimaged/partimaged.csr -out /etc/partimaged/partimaged.cert -signkey /etc/partimaged/partimaged.key")
os.system("rm /etc/partimaged/partimaged.csr")
os.system("chmod 600 /etc/partimaged/partimaged.key")
os.system("chmod 600 /etc/partimaged/partimaged.cert")
os.system("chown partimag:root /etc/partimaged/partimaged.key")
os.system("chown partimag:root /etc/partimaged/partimaged.cert")