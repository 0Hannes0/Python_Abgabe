# Dokumentation

## Inhaltsverzeichnis
1. [Einleitung](#1-einleitung)
2. [Grundlegender Aufbau des Spiels](#2-grundlegender-aufbau-des-spiels)
   - [Benutzeroberfläche](#21-benutzeroberfläche)
   - [Programmablauf](#22-programmablauf)
3. [Architektur und Klassendesign](#3-architektur-und-klassendesign)
   - [Klassendiagramm](#31-klassendiagramm)
   - [Erklärung der Klassen](#32-erklarung-der-klassen)
4. [Ordnerstruktur](#4-ordnerstruktur)
5. [Versionen der Bibliotheken](#5-versionen-der-bibliotheken)
6. [Testergebnisse](#6-testergebnisse)

## 1. Einleitung
In dieser Dokumentation wird der grundlegende Aufbau des Spiels `Verlassene Raustation` sowie die Architektur detailiert anhand von Diagrammen erklärt. Es wird außerdem die Ordnerstruktur sowie die Ergebnisse von dazu passenden Unittests dokumentiert. Um das Spiel zu starten muss man sich im Hauptordner des Spiels `PYTHON_ABGABE` befinden und in der Konsolen folgenden Befehl eingeben: `PYTHONPATH=$(pwd) python src/main.py`

## 2. Grundlegender Aufbau des Spiels

### 2.1 Benutzeroberfläche

<table style ="padding-bottom: 100px;">
  <tr>
    <td style="border: none; width: 320px; padding-bottom: 50px;"><img src="pictures/size.png"></td>
    <td style="border: none; padding-bottom: 50px;"> Als erstes soll man  die Größe des Spielfelds eingeben, dabei wird die Eingabe auf ungültige Eingaben überprüft und der Benutzer passend über eine falsche Eingabe informiert. Eine falsche Eingabe ist dann der Fall, wenn der Benutzer keine Zahl eingibt, oder keine Zahl zwischen 5 und 15.</td>
  </tr>
  <tr>
    <td style="border: none; padding-bottom: 50px;"><img src="pictures/gameboard.png" style="width: 1000px;"></td>
    <td style="border: none; padding-bottom: 50px;">Hier wird das Spielfeld ausgegeben. Die nicht aufgedeckten Felder sind hierbei ein ■ und über den Feldern wird die Zeilen-/Spaltennummer angezeigt, sodass der Benutzer leichter ein Feld auswählen kann.</td>
  </tr>
  <tr>
    <td style="border: none; padding-bottom: 50px;"><img src="pictures/choose.png" style="width: 1000px;"></td>
    <td style="border: none; padding-bottom: 50px;">Hier soll der Benutzer die Zeilen-/Spaltennummer eingeben, von dem Feld, welches er auswählen möchte. Es wird außerdem wieder auf falsche Eingaben hingewiesen.</td>
  </tr>
  <tr>
    <td style="border: none; padding-bottom: 50px;"><img src="pictures/gameboard2.png" style="width: 200px;"></td>
    <td style="border: none; padding-bottom: 50px;">Hier wird das aktualisierte Spielfeld angezeigt. Die Zahlen stehen für die Anzahl der Fallen, welche das Feld um sich herum hat. Dabei kommt dazu, dass es leere Felder gibt, da sie keine Fallen um sich herum haben und somit eigentlich eine 0 sind.</td>
  </tr>
  <tr>
    <td style="border: none; padding-bottom: 50px;"><img src="pictures/gameboard3.png" style="width: 240px;"></td>
    <td style="border: none; padding-bottom: 50px;">Hier wird das Spielfeld angezeigt, wenn man eine Fallen getroffen hat. Dabei werden alle übrigen Fallenfelder angezeigt und der Benutzer darüber informiert, dass er verloren hat.</td>
  </tr>
  <tr>
    <td style="border: none; padding-bottom: 50px;"><img src="pictures/gameboard4.png" style="width: 280px;"></td>
    <td style="border: none; padding-bottom: 50px;">Hier wird das Spielfeld angezeigt, wenn man alle freien Felder aufgedeckt hat und somit das Spield gewonnen hat.</td>
  </tr>
  <tr>
    <td style="border: none; padding-bottom: 50px;"><img src="pictures/again.png" style="width: 300px;"></td>
    <td style="border: none;">Hier wird der finale Schritt gezeigt, bei der gefragt wird ob der Benutzer erneut spielen möchte oder nicht. Fall er möchte und 'y' eingibt, geht das Spiel von vorne los. Falls er 'n' eingibt, wird das Spiel beendet.</td>
  </tr>
 </table>

### 2.2 Programmablauf

<img src= "pictures/PAP.drawio.png" alt="Programmablaufplan">

---

## 3. Architektur und Klassendesign

### 3.1 Klassendiagramm
<img src= "pictures/Klassendiagramm.drawio.png" alt="Klassendiagramm">

### 3.2 Erklärung der Klassen

## `main.py`

Hier ist der Einstiegspunkt für das Spiel. Es wird ein `Game`-Objekt erstellt und das Spiel gestartet.

---

### Methodenbeschreibung

#### `main() -> None`
**Beschreibung:**  
Startet das Spiel, indem ein `Game`-Objekt erstellt und dessen `start()`-Methode aufgerufen wird.

**Effekt:**  
- Erstellt eine Instanz der `Game`-Klasse.  
- Ruft die `start()`-Methode auf, um das Spiel zu starten.  

---

## Klasse `Game`

Die Klasse `Game` verwaltet die Spiellogik des Spiels. Sie steuert den Ablauf, verarbeitet Spielzüge und überwacht den Spielstatus.

#### Attribute
- `minSize` (*int*): Minimale Spielfeldgröße (5).
- `maxSize` (*int*): Maximale Spielfeldgröße (15).  

---

### Methodenbeschreibung

#### `__init__(self) -> None`
Initialisiert eine neue Instanz des Spiels.

**Effekt:**  
- Setzt `minSize` und `maxSize` für die Spielfeldgröße.  
- Initialisiert `_gameBoard` auf `None`.  
- Setzt `_size` auf `0` und `_moves` auf `0`.  

**Attribute:**  
- `_gameBoard` (*Board | None*): Referenz auf das Spielfeld (`None`, falls nicht initialisiert).  
- `_size` (*int*): Größe des Spielfelds.  
- `_moves` (*int*): Anzahl der bereits ausgeführten Züge.  

---

#### `_getGameBoard(self) -> Board`
**Beschreibung:**  
Gibt das aktuelle Spielfeld zurück.

**Effekt:**  
- Falls `_gameBoard` nicht initialisiert ist, wird eine `AssertionError` ausgelöst.  

**Rückgabewert:**  
- `Board` – Gibt das Spielfeld-Objekt zurück.

---

#### `start(self) -> None`
**Beschreibung:**  
Startet das Spiel und beginnt die Spielschleife.

**Effekt:**  
- Zeigt eine Willkommensnachricht an.  
- Initialisiert das Spielfeld.  
- Ruft die Hauptspiel-Schleife (`_gameLoop`) auf.  

---

#### `_end(self) -> None`
**Beschreibung:**  
Beendet das aktuelle Spiel.

**Effekt:**  
- Fragt den Spieler, ob er erneut spielen möchte.  
- Startet ein neues Spiel oder beendet das Programm je nach Nutzereingabe.  

---

#### `_initializeGameBoard(self) -> None`
**Beschreibung:**  
Erstellt das Spielfeld basierend auf der Nutzereingabe.

**Effekt:**  
- Fragt den Nutzer nach der gewünschten Spielfeldgröße.  
- Überprüft die Eingabe auf Gültigkeit.  
- Erstellt ein `Board`-Objekt mit der gewählten Größe.  

---

#### `_gameLoop(self) -> None`
**Beschreibung:**  
Führt die Hauptspiel-Schleife aus.

**Effekt:**  
- Fragt den Nutzer nach einer Zelle zum Aufdecken.  
- Überprüft die Eingabe auf Gültigkeit.  
- Führt den Zug mit `_handleMove` aus.  
- Überprüft den Spielstatus (gewonnen/verloren).  
- Falls das Spiel endet, wird `_end()` aufgerufen.  

---

#### `_handleMove(self, x: int, y: int) -> GameState`
**Beschreibung:**  
Führt einen Spielzug an der angegebenen Position aus.

**Effekt:**  
- Überprüft, ob die gewählte Zelle bereits aufgedeckt wurde.  
- Falls eine Falle getroffen wurde, verliert der Spieler (`GameState.LOST`).  
- Falls keine Falle vorhanden ist, wird das Spielfeld aktualisiert.  
- Prüft, ob der Spieler gewonnen hat.  

**Parameter:**  
- `x` (*int*): X-Koordinate der gewählten Zelle.  
- `y` (*int*): Y-Koordinate der gewählten Zelle.  

**Rückgabewert:**  
- `GameState` – Aktueller Spielstatus (`WON`, `LOST`, `PLAYING`, `REPEAT`).

---

## Klasse `Board`

Die Klasse `Board` repräsentiert das Spielfeld des Spiels. Sie verwaltet die Spielfeldzellen, platziert Fallen und ermöglicht das Aufdecken von Zellen.

---

### Methodenbeschreibung

#### `__init__(self, size: int) -> None`
**Beschreibung:**  
Erstellt ein quadratisches Spielfeld mit der angegebenen Größe.

**Attribute:**  
- `_size` (*int*): Die Größe des Spielfelds.  
- `_grid` (*list[list[Cell]]*): 2D-Liste, die die Spielfeldzellen speichert.  

**Parameter:**  
- `size` (*int*): Seitenlänge des Spielfelds.  

---

#### `getCell(self, x: int, y: int) -> Cell`
**Beschreibung:**  
Gibt die Zelle an den angegebenen Koordinaten zurück.

**Rückgabewert:**  
- `Cell` – Die Zelle an den gegebenen Koordinaten.  

---

#### `displayBoard(self) -> None`
**Beschreibung:**  
Gibt das aktuelle Spielfeld in der Konsole aus.

**Effekt:**  
- Zeigt das Spielfeld mit Zeilen- und Spaltennummern zur besseren Orientierung an.  

---

## Klasse `Cell`

Die Klasse `Cell` repräsentiert eine einzelne Zelle im Spielfeld (`gameBoard`). Sie speichert Informationen darüber, ob eine Zelle eine Falle ist, ob sie schon aufgedeckt wurde und wie viele Fallen sich in ihrer direkten Nachbarschaft befinden.

---

### Methodenbeschreibung

#### `__init__(self, isTrap: bool = False)`
Initialisiert eine Zelle. (Konstruktor)

**Parameter:**
- `isTrap` (*bool*): Gibt an, ob die Zelle eine Falle enthält (Standard: `False`).

**Attribute:**
- `_isTrap` (*bool*): Speichert, ob die Zelle eine Falle ist.
- `_adjacentTraps` (*int*): Speichert die Anzahl der Fallen in den benachbarten Zellen (Standard: `0`).
- `_isScanned` (*bool*): Gibt an, ob die Zelle bereits aufgedeckt wurde (Standard: `False`).

---

#### `scan(self) -> None`
**Beschreibung:**  
Markiert die Zelle als aufgedeckt.

**Effekt:**  
- Setzt `_isScanned` auf `True`, sodass die Zelle nicht erneut aufgedeckt werden kann.

---

## Klasse `OutOfRangeError`

Die Klasse `OutOfRangeError` ist für den Fehler, dass eine Benutzereingabe außerhalb eines vorgegebenen Wertebereichs ist.

---

### Methodenbeschreibung

#### `__init__(self, value: int, minValue: int, maxValue: int) -> None`
**Parameter:**  
- `value` (*int*): Der ungültige Wert.  
- `minValue` (*int*): Die minimale erlaubte Grenze.  
- `maxValue` (*int*): Die maximale erlaubte Grenze.  

**Attribute:**  
- `_value` (*int*): Speichert den ungültigen Wert.  
- `_min` (*int*): Speichert die untere Grenze des gültigen Bereichs.  
- `_max` (*int*): Speichert die obere Grenze des gültigen Bereichs.  

---

#### `__str__(self) -> str`
**Beschreibung:**  
Gibt eine formatierte Fehlermeldung zurück, die angibt, dass der Wert außerhalb des gültigen Bereichs liegt.

**Rückgabewert:**  
- *str* – Fehlermeldung im Format `"<Wert> is out of the Possible Range (<min>-<max>)"`  


## 4. Ordnerstruktur

```
PYTHON_ABGABE
│── src
│   ├── cell.py
│   ├── errors.py
│   ├── game.py
│   ├── gameBoard.py
│   └── main.py
│── tests
│   ├── testBoard.py
│   ├── testCell.py
│   ├── testErrors.py
│   ├── testGame.py
│   └── testMain.py
│── .pylintrc
│── mypy.ini
│── README.md
└── requirements.txt
```

## 5. Versionen der Bibliotheken
```ini
astroid==3.3.8
coverage==7.6.12
dill==0.3.9
isort==6.0.1
mccabe==0.7.0
mypy==1.15.0
mypy-extensions==1.0.0
platformdirs==4.3.6
pylint==3.3.4
tomlkit==0.13.2
typing_extensions==4.12.2
```

## 6. Testergebnisse

### mypy
<img style="width: 400px;" src="pictures/mypy.png">

### pylint
- **src**
  <img style="width: 450px;" src="pictures/pylint_src.png">
- **tests**
  <img style="width: 450px;" src="pictures/pylint_tests.png">

### unittest
<img style="width: 400px;" src="pictures/unittests.png">

### coverage
<img style="width: 400px;" src="pictures/coverage.png">

