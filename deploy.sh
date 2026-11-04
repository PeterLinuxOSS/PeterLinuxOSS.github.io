#!/bin/sh
# Nasadí stránku na lokálny nginx (127.0.0.1:8096 → tunel backup → peterlinuxos.me)
set -e
cd "$(dirname "$0")"
install -d /var/www/peterlinuxos
install -m 644 index.html /var/www/peterlinuxos/index.html
echo "deployed to /var/www/peterlinuxos"
