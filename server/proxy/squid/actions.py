#!/usr/bin/python
# -*- coding: utf-8 -*- 
#
# Copyright 2005,2006 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir = "squid-2.5.STABLE14"

def setup():
    shelltools.export("WANT_AUTOCONF", "2.1")
    autotools.autoconf()
    shelltools.export("CC", get.CC())
    autotools.configure("--prefix=/usr \
                         --bindir=/usr/bin \
                         --exec-prefix=/usr \
                         --sbindir=/usr/sbin \
                         --localstatedir=/var \
                         --mandir=/usr/share/man \
                         --sysconfdir=/etc/squid \
                         --libexecdir=/usr/lib/squid \
                         --enable-auth=\"basic,digest,ntlm\" \
                         --enable-removal-policies=\"lru,heap\" \
                         --enable-digest-auth-helpers=\"password\" \
                         --enable-basic-auth-helpers=\"LDAP,MSNT,NCSA,PAM,SMB,YP,getpwnam,multi-domain-NTLM,SASL,winbind\" \
                         --enable-external-acl-helpers=\"ip_user,ldap_group,unix_group,wbinfo_group,winbind_group\" \
                         --enable-ntlm-auth-helpers=\"SMB,fakeauth,no_check,winbind\" \
                         --enable-linux-netfilter \
                         --enable-ident-lookups \
                         --enable-useragent-log \
                         --enable-cache-digests \
                         --enable-delay-pools \
                         --enable-referer-log \
                         --enable-truncate \
                         --enable-arp-acl \
                         --with-pthreads \
                         --with-large-files \
                         --enable-htcp \
                         --enable-carp \
                         --enable-poll \
                         --enable-ssl \
                         --host=%s" %  get.HOST())

#    pisitools.dosed("include/autoconf.h", "#define SQUID_MAXFD", "#define SQUID_MAXFD 8192")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    pisitools.dodir("/var/cache/squid")
    pisitools.dodir("/var/log/squid")
    pisitools.dosym("/usr/lib/squid/errors/English", "/etc/squid/errors")
    pisitools.dodoc("CONTRIBUTORS", "CREDITS", "ChangeLog", "QUICKSTART", "SPONSORS", "doc/*.txt", "helpers/ntlm_auth/no_check/README.no_check_ntlm_auth")
    pisitools.dodoc("helpers/basic_auth/SASL/squid_sasl_auth*")
    pisitools.doman("helpers/basic_auth/LDAP/*.8")
    pisitools.dohtml("helpers/basic_auth/MSNT/README.html", "RELEASENOTES.html")
