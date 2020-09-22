# NotiaDB
*A basic database system for Python.*

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

db = db.NotiaDB("name")
name = input("Your name: ")
db.write(name=name)
new_name = input("New Name: ")
db.update("name", name=new_name)
```

### Other
```
-start_from_scratch(**kwargs): Start from scratch.
-readKeys(): Reads only keys in the file
-readValues(): Reads only values in the file
-readFile(): Reads all the file
```

### Example High Score Save Project
```py
from random import randint
import notiadb as db

db = db.NotiaDB("scores")

number = randint(1, 3)
score = 0

try:
    high_score = db.read("high_score")
except FileNotFoundError:
    db.startFromScratch(high_score=0)
    high_score = db.read("high_score")

while 1:
    guess = int(input("Guess: "))
    if guess == number:
        score += 1
        number = randint(1, 3)
    else:
        if score > high_score:
            db.update("high_score", high_score=score)
            high_score = db.read("high_score")
        print(f"Score: {score} | High Score: {high_score}")
        break
```
