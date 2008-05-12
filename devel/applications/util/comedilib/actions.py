#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2007 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-etc-hotplug \
                         --disable-docbook-binding \
                         --disable-ruby-binding \
                         --disable-static \
                         --localstatedir=/var")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodir("/var/lib/comedi/calibrations")

    # remove pcmcia config files. pcmcia unsupported by comedi
    pisitools.removeDir("/etc/pcmcia")

    # needed demo programs added
    files =["demo/antialias", "demo/ao_waveform", "demo/apply_cal", "demo/cmd", "demo/dio", \
            "demo/ao_mmap", "demo/board_info", "demo/do_waveform", "demo/ledclock", \
            "demo/gpct_buffered_counting", "demo/gpct_encoder", "demo/gpct_pulse_generator",\
            "demo/gpct_simple_counting", "demo/eeprom_dump", "demo/inp", "demo/inpn",\
            "demo/insn","demo/mmap","demo/outp", "demo/poll","demo/choose_clock", "demo/choose_filter",\
            "demo/receiver","demo/select","demo/sender","demo/choose_routing",\
            "demo/sigio","demo/sv","demo/tut1", "demo/tut2","demo/README" ]

    for data in files:
        pisitools.insinto("/usr/share/comedilib/demo",data)

    # add docs and man's
    pisitools.doman("doc/man/*.3")
    pisitools.dohtml("doc/doc_html/*")
    pisitools.dodoc("AUTHORS","COPYING","README","TODO","ChangeLog","NEWS","doc/FAQ")
