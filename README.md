# peterlinuxos.me

Osobná stránka Petra Riga. Statický web v dvoch jazykoch: `/` (SK) a `/en/` (EN).

## Úpravy

Obsah sa upravuje **len v `_src/index.html`**. `index.html` a `en/index.html` sú generované:

```sh
python3 build.py     # _src/index.html → index.html + en/index.html
./deploy.sh          # build + nasadenie na lokálny nginx (peterlinuxos.me)
```

V šablóne sú obe jazykové verzie vedľa seba:

- prvky: `<span lang="sk">…</span><span lang="en">…</span>` (funguje pre `span`, `b`, `small`, `figcaption`)
- atribúty a text mimo prvkov: `[[slovensky||english]]`

Písma (`fonts/`) sú hostované lokálne, stránka nenačítava nič z cudzích serverov.
Kópia beží aj na GitHub Pages (https://peterlinuxoss.github.io/), canonical ukazuje na peterlinuxos.me.
