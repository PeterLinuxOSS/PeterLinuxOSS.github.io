#!/bin/sh
# Nasadí stránku na lokálny nginx (127.0.0.1:8096 → tunel backup → peterlinuxos.me)
set -e
cd "$(dirname "$0")"
install -d /var/www/peterlinuxos/media
install -m 644 index.html robots.txt sitemap.xml /var/www/peterlinuxos/
# IndexNow kľúč (<32 hex>.txt v koreni)
install -m 644 ????????????????????????????????.txt /var/www/peterlinuxos/
install -m 644 media/* /var/www/peterlinuxos/media/
echo "deployed to /var/www/peterlinuxos"
