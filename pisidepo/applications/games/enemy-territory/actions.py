#
#Pardox pardox2006 at hotmail dot com
#

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

WorkDir = "."
NoStrip = "/"

def install():
    shelltools.system("sh et-linux-2.60.x86.run --noexec --keep")
    shelltools.cd("build-install-2.60")
#   GAMES_CHECK_LICENSE="yes"
#   shelltools.system("less EULA_Wolfenstein_Enemy_Territory.txt")
#   GAMES_CHECK_LICENSE="yes"#
#   shelltools.system("echo Wolfenstein Enemy Territory Oyunun tehlif hakkini kabul etmis bulunuyorsunuz")
#   shelltools.system("echo Sayet kabul etmiyorsaniz lutfen ctrl+c basip kurulumu iptal ediniz")
#   shelltools.system("sleep 20")  lisans kismi eksik oldu :(
#   kill $$  # Script kills its own process here.

    pisitools.dodoc("CHANGES", "README")
    pisitools.insinto("/opt/enemy-territory", "bin/Linux/x86/et.x86")
    pisitools.insinto("/opt/enemy-territory/Docs", "Docs/*")
    pisitools.insinto("/opt/enemy-territory/etmain", "etmain/*")
    pisitools.insinto("/opt/enemy-territory/pb", "pb/*")
    pisitools.insinto("/usr/share/pixmaps", "ET.xpm")
    pisitools.insinto("/opt/enemy-territory", "openurl.sh")
    pisitools.insinto("/opt/enemy-territory", "pb/pbcl.db")
    pisitools.dobin("bin/Linux/x86/et.x86", "/opt/enemy-territory")