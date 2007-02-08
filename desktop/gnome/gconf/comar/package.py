#!/usr/bin/python

def postInstall():
    GconfPathConfig = """# This file stores the addresses of config sources for GConf
# When a value is stored or requested, the sources are scanned from top to 
# bottom, and the first one to have a value for the key (or the first one 
# to be writeable) is used to load/store the data.

# See the GConf manual for details

# Look first in systemwide mandatory settings directory
xml:readonly:/etc/gconf/gconf.xml.mandatory

# To read in any mandatory settings that the Sys Admin may have created
# prior to a desktop system upgrade. The SysAdmin can stick read-only system
# wide sources in this file.
include /etc/gconf/2/local-mandatory.path

# Now see where users want us to look - basically the user can stick arbitrary 
# sources in a ~/.gconf.path file and they're inserted here
include \"$(HOME)/.gconf.path\"

# Give users a default storage location, ~/.gconf
xml:readwrite:$(HOME)/.gconf

# To read in any defaults settings that the Sys Admin may have created
# prior to a desktop system upgrade. The SysAdmin can stick default values
# system-wide in this file.
include /etc/gconf/2/local-defaults.path

# Finally, look at the systemwide defaults
xml:readonly:/etc/gconf/gconf.xml.defaults

"""

    file = open("/etc/gconf/2/path", "w")
    file.write(GconfPathConfig)
    file.close()