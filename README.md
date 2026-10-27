# Flask Blog Application

Eine einfache Webanwendung auf Basis von Python und Flask, die Blogbeiträge aus einer lokalen JSON-Datei liest, neu anlegt, bearbeitet und löscht (CRUD-Operationen).

## Funktionen

- **Startseite (`/`)**: Lädt alle Beiträge dynamisch aus `blogposts.json` und zeigt sie an.
- **Beitrag erstellen (`/add`)**: Nimmt Eingaben über ein HTML-Formular entgegen (POST) und speichert den neuen Beitrag mit generierter ID.
- **Beitrag bearbeiten (`/update/<post_id>`)**: Lädt bestehende Daten in ein vorausgefülltes Formular und überschreibt die Änderungen in der JSON-Datei.
- **Beitrag löschen (`/delete/<post_id>`)**: Entfernt den ausgewählten Beitrag über einen POST-Request aus der Datei.

## Technischer Aufbau

- **Backend**: Python 3, Flask
- **Templating**: Jinja2
- **Datenhaltung**: Lokale `blogposts.json` via Pythons standardmäßigem `json`-Modul
- **Frontend**: Plain HTML5, CSS3 (`static/style.css`)

## Projektstruktur

```text
.
├── app.py              # Flask-Server und Routen-Logik
├── blogposts.json      # Lokaler Datenspeicher
├── static/
│   └── style.css       # Layout und Styles
└── templates/
    ├── index.html      # Übersicht aller Beiträge
    ├── add.html        # Formular für neue Beiträge
    └── update.html     # Formular zum Bearbeiten
```

## Lokale Einrichtung

1. Virtuelle Umgebung erstellen und aktivieren:
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   ```

2. Flask installieren:
   ```bash
   pip install flask
   ```

3. Anwendung starten:
   ```bash
   python app.py
   ```

4. Im Browser aufrufen: `http://localhost:5001`