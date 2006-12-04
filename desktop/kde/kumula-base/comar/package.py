#!/usr/bin/python

import os
import time

def postInstall():
    if not os.access("/var/lib/mysql/mysql", os.F_OK):
        os.system("/usr/sbin/mysqld --user=mysql \
                                        --skip-grant-tables \
                                        --basedir=/usr \
                                        --datadir=/var/lib/mysql \
                                        --skip-innodb \
                                        --skip-bdb \
                                        --max_allowed_packet=8M \
                                        --net_buffer_length=16K \
                                        --socket=/var/run/mysqld/mysqld.sock \
                                        --pid-file=/var/run/mysqld/mysqld.pid &")

        os.system('/usr/bin/mysql --socket=/var/run/mysqld/mysqld.sock \
                                  -hlocalhost \
                                  -uroot \
                                  kumula < %s' % '/opt/kumula/sql/kumula-base.mysql')
	
        os.system('/usr/bin/mysql --socket=/var/run/mysqld/mysqld.sock \
                                  -hlocalhost \
                                  -uroot \
                                  kumula < %s' % '/opt/kumula/sql/countries.mysql')
