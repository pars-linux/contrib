#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.system("ruby setup.rb config --prefix=/usr \
                                            --std-ruby=/usr/lib/ruby/site_ruby/1.8 \
                                            --site-ruby=/usr/lib/ruby/site_ruby/1.8 \
                                            --rb-dir=/usr/lib/ruby/site_ruby/1.8 \
                                            --so-dir=/usr/lib/ruby/site_ruby/1.8 \
                                            --ruby-path=/usr/bin/ruby \
                                            --ruby-prog=/usr/bin/ruby \
                                            --without-ext")

def build():
    shelltools.system("ruby setup.rb setup")

def install():
    shelltools.system("ruby setup.rb install --prefix=%s" % get.installDIR())

    pisitools.insinto("%s/%s/html" % (get.docDIR(), get.srcTAG()), "doc/faq/*")
    pisitools.insinto("%s/%s/html" % (get.docDIR(), get.srcTAG()), "api" )

    pisitools.dodoc("ChangeLog", "README")
