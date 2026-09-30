# Baut aus quelle/tdg-umsetzung.html + quelle/daten.json:
#   wordpress-einbettung.html  -> in WordPress-Block «Individuelles HTML» einfügen
#   vorschau.html              -> lokale Vorschau (über einen lokalen Server öffnen)
import pathlib
hier = pathlib.Path(__file__).parent
ziel = hier.parent
# Hier den Ordner eintragen, in den die Bilder und Klänge in WordPress hochgeladen wurden:
WP_PFAD = 'https://www.charisarnold.ch/wp-content/uploads/2026/09/'

quelle = (hier / 'tdg-umsetzung.html').read_text(encoding='utf-8')
daten = (hier / 'daten.json').read_text(encoding='utf-8')
# Meldet im iframe die Höhe an die einbettende Seite (WordPress passt das iframe an).
HOEHE = """<script>(function(){if(window.parent===window)return;document.documentElement.style.overflowY="hidden";var l=0;function m(){var el=document.getElementById('tdg-prozess');if(!el)return;var h=Math.ceil(el.getBoundingClientRect().bottom+window.scrollY);if(h!==l){l=h;window.parent.postMessage({tdgHoehe:h},'*');}}new ResizeObserver(m).observe(document.getElementById('tdg-prozess'));window.addEventListener('load',m);setInterval(m,1000);})();</script>"""

def baue(bild, klang):
    return quelle.replace('__DATEN__', daten).replace('__BILDPFAD__', bild).replace('__KLANGPFAD__', klang)
(ziel / 'wordpress-einbettung.html').write_text(baue(WP_PFAD, WP_PFAD), encoding='utf-8')
seite = ('<!doctype html><html lang="de"><head><meta charset="utf-8">'
         '<meta name="viewport" content="width=device-width,initial-scale=1">'
         '<title>Umsetzungsprozess – Topografie der Gefühle</title>'
         '<style>body{margin:0;background:#fff}</style></head><body>'
         + baue('bilder/', 'klaenge/') + HOEHE + '</body></html>')
(ziel / 'vorschau.html').write_text(seite, encoding='utf-8')
(ziel / 'index.html').write_text(seite, encoding='utf-8')  # für GitHub Pages / iframe
print('ok', len(seite))
