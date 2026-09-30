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
def baue(bild, klang):
    return quelle.replace('__DATEN__', daten).replace('__BILDPFAD__', bild).replace('__KLANGPFAD__', klang)
(ziel / 'wordpress-einbettung.html').write_text(baue(WP_PFAD, WP_PFAD), encoding='utf-8')
seite = ('<!doctype html><html lang="de"><head><meta charset="utf-8">'
         '<meta name="viewport" content="width=device-width,initial-scale=1">'
         '<title>Umsetzungsprozess – Topografie der Gefühle</title>'
         '<style>body{margin:0;background:#fff}</style></head><body>'
         + baue('bilder/', 'klaenge/') + '</body></html>')
(ziel / 'vorschau.html').write_text(seite, encoding='utf-8')
print('ok', len(seite))
