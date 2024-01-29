# Git Workshop: Rebase Aufgabe

#### Ihr müsst keine Dateien von Hand anfassen! Die Gesamte Übung kann (und sollte) nur mit `git ...` Kommandos gelöst werden!

## Wozu git rebase nutzen?
- mit `git rebase` könnt ihr Änderunen einer anderen Branch auf eure Übernehmen, ohne Merge Commit
- Beispiel: ihr zweigt von `master` ab, entwickelt euer Feature. Eine andere Branch wird in `master` gemerged. Jetzt könnt ihr die Änderungen mit `git rebase master` in eure Branch übernehmen.
- Oder: ihr zweigt von `master` ab um einen fix zu bauen, der aber eigentlich auf eine ältere Release Branch sollte. Ihr könntet mit `git rebase release` eure Änderungen auf den Release-Zweig umsetzen. (Achtung: ihr würdet an dieser Stelle auch alle Änderungen zwischen release und master mitnehmen! Hier eignet sich mMn ein Stash oder Cherry Pick besser)
- Vorteil ggü `git merge`: es entsteht kein Merge commit, sondern es Verhält sich, als ob ihr direkt von dieser neuen Branch aus angefangen hättet. Die Konfliktlösung kann sich vereinfachen, weil jeder eurer Commits nacheinander auf die rebase Branch aufgesetzt wird, anstatt alle Änderungen gleichzeitig zu übernehmen.
- mit dem Interaktiven Rebase kann man übersichtlich Commits aus der Vergangenheit ändern, verwerfen, oder zusammenfassen
- man kann sogar eine neue upstream angegben, zB `git rebase someones_fork master`
  
## Kleiner Überblick über Funktionen:
- `git rebase <branch>` startet einen Rebase
- `git rebase -i <branch>` startet einen Interaktiven Rebase
  - lest die Kommentare, die git euch anzeigt! Da sind die einzelnen Commands wie `pick`, `drop`, `reword` und `fixup` erklärt!
- `--autosquash` fasst automatisch commits zusammen die mit `fixup!`, `squash!` oder `amend!` beginnen
  - bsp: `commit 1 - write tests`, `commit 2 - new feature`, `commit 3 - fixup! write tests`
  - commit 1 und commit 3 werden automatisch in einen Zusammengefasst. 
  - am besten mit `git commit --fixup ...` erstellen (... kann mglw. eure Shell vervollständigen!)
  - in GUI Tools einfach die Commit Message mit `fixup!` anfangen lassen 
- statt einer Branch kann man auch einen Ausdruck wie `HEAD~2` nutzen um den aktuellen Zweig auf sich selbst zu rebasen
- wenn ein Konflikt auftritt, muss man diesen lösen und mit `git rebase --continue` manuell fortfahren
- mit `git rebase --abort` kann man einen Rebase abbrechen

## Übung
- es gibt 2 branches: `master` und `develop`
- ihr habt auf develop ein neues Feature entwickelt, es ist bereit zum merge in master. 
- ein Kollege hat sein neues Feature bereits in `master` gemerged
- zieht die Änderungen vom Master Branch mithilfe von git rebase auf den Develop branch
- macht eure History hübsch, sonst wird euer MR noch abgelehnt...
    - keine "wip" commits!
    - keine typos in commits!
    - keine debugging commits!

