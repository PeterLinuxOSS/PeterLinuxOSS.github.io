#!/usr/bin/env python3
"""Zo šablóny src/index.html vyrobí index.html (SK) a en/index.html (EN).

V šablóne sú obe jazykové verzie:
  <span lang="sk">…</span><span lang="en">…</span>   prvky (span, b, small, figcaption)
  [[slovensky||english]]                              atribúty a texty mimo prvkov
Každá výstupná stránka obsahuje len svoj jazyk.
"""
import re, sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).parent
TAGS = 'span|b|small|figcaption'
NEWTAB = {'sk': 'otvorí sa v novej karte', 'en': 'opens in a new tab'}
VOID = {'meta', 'link', 'img', 'br', 'source', 'path', 'rect', 'circle'}


def render(src, lang):
    other = 'en' if lang == 'sk' else 'sk'
    out = re.sub(r'\[\[(.*?)\|\|(.*?)\]\]', lambda m: m.group(1 if lang == 'sk' else 2), src, flags=re.S)
    for m in re.finditer(rf'<({TAGS}) lang="(?:sk|en)">(.*?)</\1>', out, flags=re.S):
        assert f'<{m.group(1)}' not in m.group(2), f'vnorený <{m.group(1)}> v jazykovom prvku: {m.group(0)[:80]}'
    out = re.sub(rf'<({TAGS}) lang="{other}">.*?</\1>', '', out, flags=re.S)
    out = re.sub(rf'<({TAGS}) lang="{lang}">', r'<\1>', out)
    # odkazy do novej karty to čítačke obrazovky povedia
    out = re.sub(r'(<a\b[^>]*target="_blank"[^>]*>.*?)</a>',
                 rf'\1<span class="sr"> ({NEWTAB[lang]})</span></a>', out, flags=re.S)
    return out.replace('<!doctype html>\n', '<!doctype html>\n<!-- GENEROVANÉ z src/index.html cez build.py — neupravovať ručne -->\n', 1)


class Balance(HTMLParser):
    def __init__(self):
        super().__init__(); self.stack = []
    def handle_starttag(self, tag, attrs):
        if tag not in VOID: self.stack.append(tag)
    def handle_startendtag(self, tag, attrs):        # <path …/> v SVG
        pass
    def handle_endtag(self, tag):
        assert self.stack and self.stack[-1] == tag, f'zle uzavretý </{tag}> na riadku {self.getpos()[0]}, otvorené: {self.stack[-3:]}'
        self.stack.pop()


def check(html, lang):
    other = 'en' if lang == 'sk' else 'sk'
    assert '[[' not in html and '||' not in html.split('<script>')[0], 'zvyšok zástupného textu'
    assert not re.search(rf'<({TAGS}) lang=', html), 'zvyšok jazykového prvku'
    assert f'<html lang="{lang}">' in html
    b = Balance(); b.feed(html); assert not b.stack, b.stack


def main():
    src = (ROOT / 'src/index.html').read_text(encoding='utf-8')
    for lang, path in (('sk', 'index.html'), ('en', 'en/index.html')):
        html = render(src, lang); check(html, lang)
        (ROOT / path).parent.mkdir(exist_ok=True)
        (ROOT / path).write_text(html, encoding='utf-8')
        print(f'{path}: {len(html.encode())} B')


if __name__ == '__main__':
    sys.exit(main())
