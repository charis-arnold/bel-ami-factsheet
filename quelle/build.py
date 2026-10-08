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
# Gemessen wird die Höhe des <html>-Elements selbst: scrollHeight ist nie kleiner als das
# iframe, das iframe könnte damit nur wachsen (z. B. nach dem Schliessen eines Aufklappers).
# Die Elternseite kann die Höhe mit {type:'iframe-hoehe-anfrage'} jederzeit neu anfordern
# (falls ihr Listener erst nach den ersten Meldungen läuft, z. B. wegen «JS verzögern»).
# Die Kontrolle im Sekundentakt sendet nur bei einer Änderung.
HOEHE = """<script>
(function(){
  if (window.self === window.top) return;
  var html = document.documentElement, letzte = 0;
  html.classList.add('im-iframe');
  function melde(immer){
    var h = Math.ceil(html.getBoundingClientRect().height);
    if (h === letzte && immer !== true) return;
    letzte = h;
    window.parent.postMessage({ type: 'iframe-hoehe', height: h }, '*');
  }
  window.addEventListener('load', melde);
  window.addEventListener('message', function(e){
    if (e.source === window.parent && e.data && e.data.type === 'iframe-hoehe-anfrage') melde(true);
  });
  new ResizeObserver(melde).observe(html);
  setInterval(melde, 1000);
})();
</script>"""

def baue(bild, klang):
    return quelle.replace('__DATEN__', daten).replace('__BILDPFAD__', bild).replace('__KLANGPFAD__', klang)
(ziel / 'wordpress-einbettung.html').write_text(baue(WP_PFAD, WP_PFAD), encoding='utf-8')
seite = ('<!doctype html><html lang="de"><head><meta charset="utf-8">'
         '<meta name="viewport" content="width=device-width,initial-scale=1">'
         '<title>Umsetzungsprozess – Topografie der Gefühle</title>'
         '<style>html,body{margin:0}body{background:#fff}'
         'html.im-iframe,html.im-iframe body{overflow:hidden}</style></head><body>'
         + baue('bilder/', 'klaenge/') + HOEHE + '</body></html>')
(ziel / 'vorschau.html').write_text(seite, encoding='utf-8')
(ziel / 'index.html').write_text(seite, encoding='utf-8')  # für GitHub Pages / iframe
print('ok', len(seite))
