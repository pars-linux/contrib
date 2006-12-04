#!/usr/bin/python
import os

def postInstall():
    #os.system("/usr/sbin/groupadd -g 450 firebird")
    #os.system("/usr/sbin/useradd firebird -g firebird -s /bin/bash -d /opt/firebird -u 450")

    os.system("/usr/bin/chown -R firebird:firebird /opt/firebird")
    os.system("/usr/bin/chown firebird:firebird /var/log/firebird.log")
    
    # Read-only directories
    os.system("find /opt/firebird -type d | xargs chmod o=-w")
 