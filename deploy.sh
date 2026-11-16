#!/bin/sh
# Zostaví stránky zo _src/ a nasadí ich na lokálny nginx (127.0.0.1:8096 → tunel backup → peterlinuxos.me)
set -e
cd "$(dirname "$0")"
python3 build.py
D=/var/www/peterlinuxos
install -d $D/media $D/fonts $D/en
install -m 644 index.html 404.html robots.txt sitemap.xml favicon.ico favicon.svg apple-touch-icon.png $D/
install -m 644 en/index.html $D/en/
# IndexNow kľúč (<32 hex>.txt v koreni)
install -m 644 ????????????????????????????????.txt $D/
install -m 644 media/* $D/media/
install -m 644 fonts/* $D/fonts/
echo "deployed to $D"
