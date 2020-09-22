# NotiaDB
<<<<<<< HEAD

*A basic database system for Python.* For download [notiadb](https://pypi.org/project/notiadb/)

[![License](https://img.shields.io/badge/license-MIT-green)](https://img.shields.io/badge/license-MIT-green)
[![Version](https://img.shields.io/badge/version-0.4-blue)](https://img.shields.io/badge/version-0.4-blue)
[![Status](https://img.shields.io/badge/status-pre--alpha-red)](https://img.shields.io/badge/status-pre--alpha-red)


=======
*A basic database system for Python.* For download [notiadb](https://pypi.org/project/notiadb/)

[![License](https://img.shields.io/badge/license-MIT-green)](https://img.shields.io/badge/license-MIT-green)
[![Version](https://img.shields.io/badge/version-0.5-blue)](https://img.shields.io/badge/version-0.5-blue)
[![Status](https://img.shields.io/badge/status-pre--alpha-red)](https://img.shields.io/badge/status-pre--alpha-red)

>>>>>>> 370f332... Added filter(), id and column system, Updated update(), version0.5
## Quick Start

### write() and read()<br>
```py
import notiadb as db

db = db.NotiaDB("name")
name = input("Your name: ")
db.write(name=name)
print(db.read("name"))
```

### update()
```py
import notiadb as db

<<<<<<< HEAD
db = db.NotiaDB("name")
name = input("Your name: ")
db.write(name=name)
new_name = input("New Name: ")
db.update("name", name=new_name)
=======
db = db.NotiaDB("languages", auto_id=True)
db.write(name="Python")
db.writeNl(name="C")
db.update(db.filter("name", "C"), "name", name="C++")
>>>>>>> 370f332... Added filter(), id and column system, Updated update(), version0.5
```

### Other
```
<<<<<<< HEAD
-startFromScratch(**kwargs): Start from scratch.
-readKeys(): Reads only keys in the file
-readValues(): Reads only values in the file
-readFile(): Reads all the file
=======
-start_from_scratch(**kwargs): Start from scratch.
-readKeys(): Reads only keys in the file
-readValues(): Reads only values in the file
-readFile(): Reads all the file
-filter(key, value): Returns the dictionary with the desired key and value, returns a list if there is more than one value to return
>>>>>>> 370f332... Added filter(), id and column system, Updated update(), version0.5
```

### Example High Score Save Project
```py
from random import randint
import notiadb as db

db = db.NotiaDB("scores")

number = randint(1, 3)
score = 0

<<<<<<< HEAD
try:
    high_score = db.read("high_score")
except FileNotFoundError:
    db.startFromScratch(high_score=0)
    high_score = db.read("high_score")
=======
if db.readFile() == "File is Empty":
    db.startFromScratch(high_score=0)
high_score = db.read("high_score")
>>>>>>> 370f332... Added filter(), id and column system, Updated update(), version0.5

while 1:
    guess = int(input("Guess: "))
    if guess == number:
        score += 1
        number = randint(1, 3)
    else:
        if score > high_score:
<<<<<<< HEAD
            db.update("high_score", high_score=score)
=======
            db.update(db.readFile(), "high_score", high_score=score)
>>>>>>> 370f332... Added filter(), id and column system, Updated update(), version0.5
            high_score = db.read("high_score")
        print(f"Score: {score} | High Score: {high_score}")
        break
```
