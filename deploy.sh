#!/bin/sh
# Nasadí stránku na lokálny nginx (127.0.0.1:8096 → tunel backup → peterlinuxos.me)
set -e
cd "$(dirname "$0")"
install -d /var/www/peterlinuxos/media
install -m 644 index.html /var/www/peterlinuxos/index.html
install -m 644 media/* /var/www/peterlinuxos/media/
echo "deployed to /var/www/peterlinuxos"
