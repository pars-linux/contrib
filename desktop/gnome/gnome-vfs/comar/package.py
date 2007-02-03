import os

def postInstall():
    os.system("gconftool-2 --install-schema-file=/etc/gconf/schemas/desktop_default_applications.schemas")
    os.system("gconftool-2 --install-schema-file=/etc/gconf/schemas/desktop_gnome_url_handlers.schemas")
    os.system("gconftool-2 --install-schema-file=/etc/gconf/schemas/system_dns_sd.schemas")
    os.system("gconftool-2 --install-schema-file=/etc/gconf/schemas/system_http_proxy.schemas")
    os.system("gconftool-2 --install-schema-file=/etc/gconf/schemas/system_smb.schemas")
