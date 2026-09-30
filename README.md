# Topografie der Gefühle – Umsetzungsprozess

Interaktive Fassung von Seite 2 des Factsheets, gebaut mit p5.js. Die Seite zeigt, worauf sich die visuelle Gestaltung des Projekts [bel-ami.ch](https://bel-ami.ch/) bezieht: Zeitgenossen aus dem Paris von 1885 (Maupassant, Pissarro, Haussmann, Saint-Saëns, Eiffel/Laloux, Fournier, Commission du Vieux Paris) und die Gestaltungselemente, die aus ihnen entstanden sind. Alle Verbindungen laufen in der Kreisgrafik zusammen.

## Dateien

- `quelle/tdg-umsetzung.html` – Quelltext (HTML, CSS, p5.js)
- `quelle/daten.json` – Daten aus dem Projekt `bel-ami` (Kapitel, Orte, Routen, Fotomarker, Grundkarte)
- `quelle/build.py` – baut die beiden Ausgabedateien
- `vorschau.html` – lokale Vorschau
- `wordpress-einbettung.html` – Code für den WordPress-Block «Individuelles HTML»
- `bilder/`, `klaenge/` – Bilder und Klänge (Samples aus VCSL, CC0)

## Bauen und ansehen

```sh
python3 quelle/build.py      # WP_PFAD in build.py vorher auf den Upload-Ordner setzen
python3 -m http.server       # dann http://localhost:8000/vorschau.html öffnen
```

## In WordPress einbauen

1. Den Inhalt von `bilder/` und `klaenge/` in die Mediathek hochladen.
2. `WP_PFAD` in `quelle/build.py` auf diesen Ordner setzen und das Skript ausführen.
3. Den Inhalt von `wordpress-einbettung.html` in einen Block «Individuelles HTML» einfügen.

CAS Generative Data Design · Charis Arnold · September 2026
