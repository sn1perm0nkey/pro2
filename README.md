# Körperwerte und Jogging

## Projektidee
Ich habe im Sommer 2022 mich öfters gewogen und bin (viel weniger :D) joggen gegangen. Ich habe soviel bzw. wenig gegessen, dass ich ein Kaloriendefizit hatte. Die Daten vom wiegen und joggen habe ich festgehalten.
Ich wollte nun ein Tool erstellen, bei dem ich diese Daten eingeben kann und dann Statistiken sowie eine schöne Darstellung der Einträge sehen kann. Zusätzlich ist auch noch der Hintergedanke, dass ich wieder damit beginne, meine Daten festzuhalten. Dabei kann ich dieses Tool dann verwenden.

## Installation
Wenn man auf github im Bereich des Repositorys ist, muss man in den Reiter "Code" gehen. Dort ist ein Dropdown-Button der ebenfalls "Code" heisst vorzufinden. Nachdem man auf diesen geklickt hat, kann man die angezeigte URL kopieren.

Ich empfehle, die Community Version von PyCharm zu verwenden. PyCharm muss zwingend richtig aufgesetzt sein, das heisst Python MUSS ebenfalls installiert und mit PyCharm verbunden sein. Wenn man PyCharm öffnet, kann man dann auf "Get from VCS" klicken. Danach muss man bei "Version control" "Git" auswählen. Beim Feld von "URL" kann man nun die zuvor kopierte URL einfügen. Im nächsten Schritt muss man noch den Ordner auswählen, in welchem das lokale Repository erstellt werden soll. Um abzuschliessen muss man nun noch auf "Clone" klicken.

Um das Projekt zu starten, muss man oben rechts "main" einstellen und auf das "Play Symbol", also "Run 'main'", klicken. Nun erscheint in der Konsole ein Link. Man muss nun lediglich noch auf diesen Link klicken und dann öffnet sich auch schon dieses Projekt.

## Funktionen und Benutzung
### Dateneingabe
Beim Start landet man automatisch auf dieser Seite, aber man kann auch in der Navbar ganz links auf "neuer eintrag" klicken. Hier kann man nun die Kategorie auswählen, also ob man die Daten vom Joggen oder die Daten, welche einem die eigene Waage gibt, eintragen will. Um die Daten der Waage einzutragen ist es wichtig, dass man eine Waage hat, welche folgende Daten bereitstellen kann: Gewicht in kg, Körperfettanteil in %, Körperwasseranteil in %, Muskelanteil in % sowie der BMI (Mir ist klar, dass eine Waage eher keine korrekten Daten messen kann, jedoch sind diese Daten meistens relativ gleich genau gemessen und somit kann man seine Fortschritte trotzdem gut nachverfolgen). Um Daten vom Joggen einzutragen, muss man die Strecke sowie die Zeit messen.

Nachdem man eine Kategorie ausgewählt hat, kann man die vorher genannten Daten einfügen und anschliessend auf "Senden" klicken. Die Felder werden anschliessend wieder leer sein, damit man gleich die nächsten Daten eintragen kann, falls man mehrere Messungen auf einmal eintragen möchte.

### Datenausgabe
Bei der Navbar kann man nun noch entweder auf "statistik" oder auf "listen" klicken. Bei beiden Seiten kann man wie zuvor schon die Kategorie auswählen.
Bei "statistik" sieht man Liniendiagramme, welche aus den eingespiesenen Daten erzeugt werden.
Bei "listen" sieht man die übersichtliche Auflistung der eingespiesenen Daten. Dieses Programm erzeugt aus den eingespiesenen Daten auch noch neue Daten wie z.B. der Körperfettanteil in kg. Diese neuen Daten sind ebenfalls in der Tabelle sowie in den Statistiken zu finden.

### Datenverarbeitung
Bei "listen" gibt es noch weitere Funktionen. Man kann in der Spalte "Auswählen" auf den Radiobutton klicken. Ist dieser rot, so ist diese Zeile ausgewählt. Man kann nun unter der Tabelle entweder auf "Bearbeiten" oder auf "Löschen" klicken.
Klickt man auf "Bearbeiten", so kommt erneut das Eingabeformular. Hier kann man die Daten des Eintrags, welcher ausgewählt war, anpassen, falls diese z.B. falsch sind. Wenn man auf Abbrechen klickt, wird die Änderung abgebrochen und nicht abgespeichert. Wenn man auf Senden klickt, werden die Daten des Eintrags aktualisiert.
Klickt man unter der Liste auf "Löschen", so wird der ausgewählte Eintrag entfernt.

### Funktionslos
Oben rechts befindet sich noch der Benutzername. Dieser ist beim aktuellen Stand des Projektes auf "grafrob" gesetzt und es passiert nichts, wenn man diesen anklickt. Für ein zukünftiges Update kann man sich an dieser Stelle anmelden, um die Daten in einem eigenen Account zu speichern und so mit anderen zu teilen.

## Schlusswort
Mir macht das Programmieren mit Python sowie mit HTML/CSS sehr viel Spass. In diesem Projekt konnte ich beides kombinieren, wodurch ich immer wieder nach vielen Stunden vertieftem arbeiten erst gemerkt habe, wie lange ich eigentlich wieder ohne Pausen am arbeiten war.

Ich habe zufälligerweise im Sommer 2022 aus Lust und Laune mit Python und vielen Tutorials einen "Discord Bot" erstellt. Ich konnte bei diesem Projekt festellen, dass ich viele Funktionen bereits von damals kannte. Jinja war für mich neu sowie die ganze Kombination mit HTML/CSS.

Ich bin sehr stolz auf mein Endergebnis und denke, dass ich dieses Tool tatsächlich in Zukunft verwenden und evtl., je nachdem wie viel Zeit ich zur Verfügung habe, weiter ausbauen werde.
