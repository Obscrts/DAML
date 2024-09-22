# Hotel Indoor Analyse

![Telekom Logo](resources/images/logo/telekom.png) ![FHDW Logo](resources/images/logo/fhdw.png)

## Übersicht

Dieses Projekt analysiert die Mobilfunknetzqualität innerhalb und um Hotels in verschiedenen deutschen Städten, die Austragungsorte der Fußball-Europameisterschaft 2024 waren. Das Ziel ist es, die Netzabdeckung und -leistung durch eine detaillierte Untersuchung von Metriken wie Timing Advance (TA), RSRP (Reference Signal Received Power), RSRQ (Reference Signal Received Quality) und weiteren Mobilfunkkennzahlen zu bewerten. 

Zusätzlich zur Analyse der Netzqualität in den tatsächlichen Hotelbereichen wird auch die Umgebung der Hotels mittels **Buffered Polygons** (gepufferte Polygone) untersucht. 

### Enthaltene Städte:
- Berlin
- Köln
- Dortmund
- Düsseldorf
- Frankfurt am Main
- Gelsenkirchen
- Hamburg
- Leipzig
- München
- Stuttgart

## Zielsetzung

Dieses Projekt konzentriert sich auf die Untersuchung von drei Hauptthesen:
1. **Hotels mit höherem Timing Advance (TA) haben im Durchschnitt eine schlechtere Signalqualität (RSRP, RSRQ).**
2. **Hotels mit hoher Datenübertragungsrate (DL/UL Throughput) zeigen eine bessere Signalqualität (RSRP, RSRQ).**
3. **Es existieren räumliche Cluster von Hotels mit ähnlicher Netzqualität in bestimmten geographischen Regionen.**

Die Analyse umfasst verschiedene Ansätze, wie:
- Univariate, bivariate und multivariate Analysen.
- Nutzung von Machine-Learning-Methoden wie Random Forest Regression und Lineare Regression.
- Hyperparameteroptimierung mit GridSearchCV zur Verbesserung der Modellleistung.
- Räumliche Clusteranalyse basierend auf GeoJSON-Daten.

## Inhalt

- **Datenanalyse**: Analyse der Mobilfunkmetriken TA, RSRP, RSRQ, DL/UL Throughput und Polygonflächen.
- **Machine Learning**: Modelle zur Vorhersage der Signalqualität (Random Forest, Lineare Regression).
- **Clustering**: DBSCAN- und KMeans-Clusteranalyse zur Identifizierung von räumlichen Clustern mit ähnlicher Netzqualität.
- **Datenvisualisierung**: Verschiedene Diagramme und Heatmaps zur Visualisierung von Mobilfunkdaten.

## Installation

### Voraussetzungen

Um das Projekt lokal auszuführen, musst du Python 3.x und die erforderlichen Bibliotheken installiert haben. Alle Abhängigkeiten sind in der Datei **`requirements.txt`** aufgeführt.

### Installation

1. **Repository klonen**
   
    ```bash
    git clone https://github.com/Obscrts/DAML.git
    ```

2. **Erstellen und Aktivieren eines virtuellen Environments**
Erstelle ein virtuelles Environment, um die benötigten Abhängigkeiten zu installieren:

    ```bash
    python -m venv venv
    ```

    Aktiviere das Environment:

 - Auf Windows:
    ```bash
    venv\Scripts\activate
    ```

 - Auf MacOS/Linux:
    ```bash
    source venv/bin/activate
    ```

3. **Abhängigkeiten installieren**
Installiere die benötigten Bibliotheken mit der Datei requirements.txt:

    ```bash
    pip install -r requirements.txt
    ```

4. Starten der Analyse
Führe die Jupyter-Notebook oder die Quarto-Datei aus, um die Analyse zu starten:

    ```bash
    quarto preview
    ```

## Datenquellen
Die verwendeten Mobilfunkdaten stammen von der Deutschen Telekom und wurden mit dem NitroGEO-Tool von Viavi extrahiert. Zusätzlich werden GeoJSON-Dateien zur geografischen Analyse der Hotelbereiche verwendet.

## Projektstruktur
```
├── resources/
│   ├── data/
│   │   ├── normal/                 # Daten der tatsächlichen Hotelbereiche
│   │   ├── buffered/               # Daten der gepufferten Polygone
│   │   ├── polygons/               # GeoJSON-Daten für räumliche Analysen
│   ├── images/                     # Logos und Bildmaterial
│   └── scripts/                    # Python-Skripte für Analysen
├── notebooks/                      # Jupyter-Notebooks zur explorativen Datenanalyse
├── Hotel_Indoor_Analyse.qmd        # Quarto-Datei für die Analyse
├── README.md                       # Diese README-Datei
├── requirements.txt                # Liste der Abhängigkeiten
└── .gitignore                      # Git ignore file
```

## Nutzung
Das Projekt enthält eine detaillierte Dokumentation und Visualisierungen. Um die vollständige Analyse durchzuführen, empfehle ich die Verwendung von **Quarto** oder **Jupyter Notebooks**.

## Ergebnisse und Fazit

- **These 1**: Bestätigt. Hotels mit höherem TA zeigen tendenziell eine schlechtere Netzqualität.

- **These 2**: Teils bestätigt. Höherer DL/UL Throughput ist mit besserer Signalqualität verbunden, aber der Zusammenhang ist moderat.

- **These 3**: Bestätigt. Es gibt deutliche räumliche Cluster von Hotels mit ähnlicher Netzqualität.

## Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert. Siehe die **LICENSE**-Datei für Details.