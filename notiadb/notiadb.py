<<<<<<< HEAD
import ast


class NotiaDB:
    """
        -Write Operations
        *Methods
            -write: Writes to file, if file doesn't exist create a new the file
            -start_from_scratch: Start from scratch.
            -update: Updates a value connected of key

        -Read Operations
        *Methods
            -read: Reads the file
            -readKeys: Reads only keys in the file
            -readValues: Reads only values in the file
            -readFile: Reads all the file
    """

    def __init__(self, file_name):
        self.name = file_name

    def write(self, **kwargs):
        with open(f"{self.name}.ndb", "a+", encoding="utf8") as f:
            f.seek(0)
            data = f.read()
            if len(data) == 0:
                f.write(str(kwargs))
            else:
                data = data.replace("}", ",")
                with open(f"{self.name}.ndb", "w"):
                    f.write(data + str(kwargs).replace("{", " "))

    def startFromScratch(self, **kwargs):
        with open(f"{self.name}.ndb", "w", encoding="utf8") as f:
            f.write(str(kwargs))

    def update(self, key, **kwargs):
        data = self.readFile()
        data_dict = ast.literal_eval(data)
        with open(f"{self.name}.ndb", "w", encoding="utf8") as f:
            if type(data_dict[key]) == str:
                f.seek(0)
                index = data.index(f"'{key}':")
                data_start = data[0:index + len(key) + 5]
                data_last = data[index + len(key) + 5 + len(data_dict[key]):]
                f.write(f"{data_start}{kwargs[key]}{data_last}")
            elif type(data_dict[key]) == int:
                f.seek(0)
                index = data.index(f"'{key}':")
                data_start = data[0:index + len(key) + 4]
                data_last = data[index + len(key) + 4 + len(str(data_dict[key])):]
                f.write(f"{data_start}{kwargs[key]}{data_last}")

    def read(self, key):
        with open(f"{self.name}.ndb", "r", encoding="utf8") as f:
            f.seek(0)
            if len(f.read()) > 0:
                f.seek(0)
                data = f.read()
                data_dict = ast.literal_eval(data)
                return data_dict[key]
            else:
                return "File is Empty"

    def readKeys(self):
        with open(f"{self.name}.ndb", "r", encoding="utf8") as f:
            if len(self.readFile()) > 0:
                data = self.readFile()
                data_dict = ast.literal_eval(data)
                return data_dict.keys()
            else:
                return "File is Empty"

    def readValues(self):
        with open(f"{self.name}.ndb", "r", encoding="utf8") as f:
            if len(self.readFile()) > 0:
                data = self.readFile()
                data_dict = ast.literal_eval(data)
                return data_dict.values()
            else:
                return "File is Empty"

    def readFile(self):
        with open(f"{self.name}.ndb", "r", encoding="utf8") as f:
            f.seek(0)
            if len(f.read()) > 0:
                f.seek(0)
                data = f.read()
                return data
            else:
                return "File is Empty"
=======
import ast


class NotiaDB:
    """
        -Write Operations
        *Methods
            -write: Writes to file, if file doesn't exist create a new the file
            -startFromScratch: Start from scratch.
            -update: Updates a value connected of key

        -Read Operations
        *Methods
            -read: Reads the file
            -readKeys: Reads only keys in the file
            -readValues: Reads only values in the file
            -readFile: Reads all the
            -filter(key, value): Returns the dictionary with the desired key and value, returns a list if there is more than one value to return
    """

    def __init__(self, file_name, auto_id=False):
        self.name = file_name
        f = open(f"{self.name}.ndb", "a", encoding="utf8")
        f.close()
        self.id = self.readFile().count("'id'") + 1
        self.auto_id = auto_id

    def write(self, **kwargs):
        with open(f"{self.name}.ndb", "a", encoding="utf8") as f:
            f.seek(0)
            data = self.readFile()
            if data == "File is Empty":
                if self.auto_id:
                    f.write(str(kwargs)[:1] + f"'id': {self.id}, " + str(kwargs)[1:])
                    self.id += 1
                else:
                    f.write(str(kwargs))
            else:
                data = data.replace("}", ",")
                with open(f"{self.name}.ndb", "w"):
                    f.write(data + str(kwargs).replace("{", " "))

    def writeNl(self, **kwargs):
        with open(f"{self.name}.ndb", "a", encoding="utf8") as f:
            f.seek(0)
            f.seek(len(self.readFile()))
            if self.auto_id:
                f.write("\n" + str(kwargs)[:1] + f"'id': {self.id}, " + str(kwargs)[1:])
                self.id += 1
            else:
                f.write("\n" + str(kwargs))

    def filter(self, key, value):
        with open(f"{self.name}.ndb", "r") as f:
            result = list()
            datas = f.readlines()
            for data in datas:
                if ast.literal_eval(data)[key] == value:
                    result.append(data)
            if len(result) > 1:
                return result
            elif len(result) == 1:
                return result[0]

    def startFromScratch(self, **kwargs):
        with open(f"{self.name}.ndb", "w", encoding="utf8") as f:
            f.write(str(kwargs))

    def update(self, data, key, **kwargs):
        data = data
        data_dict = ast.literal_eval(data)
        file = self.readFile().split(data)
        with open(f"{self.name}.ndb", "w", encoding="utf8") as f:
            if type(data_dict[key]) == str:
                f.seek(0)
                index = data.index(f"'{key}':")
                data_start = data[0:index + len(key) + 5]
                data_last = data[index + len(key) + 5 + len(data_dict[key]):]
                f.write(file[0])
                f.write(f"{data_start}{kwargs[key]}{data_last}")
                f.write(file[1])
            elif type(data_dict[key]) == int:
                f.seek(0)
                index = data.index(f"'{key}':")
                data_start = data[0:index + len(key) + 4]
                data_last = data[index + len(key) + 4 + len(str(data_dict[key])):]
                f.write(f"{data_start}{kwargs[key]}{data_last}")

    def read(self, key):
        with open(f"{self.name}.ndb", "r", encoding="utf8") as f:
            f.seek(0)
            if len(f.read()) > 0:
                f.seek(0)
                data = f.read()
                data_dict = ast.literal_eval(data)
                return data_dict[key]
            else:
                return "File is Empty"

    def readKeys(self):
        if len(self.readFile()) > 0:
            data = self.readFile()
            data_dict = ast.literal_eval(data)
            return data_dict.keys()
        else:
            return "File is Empty"

    def readValues(self):
        if len(self.readFile()) > 0:
            data = self.readFile()
            data_dict = ast.literal_eval(data)
            return data_dict.values()
        else:
            return "File is Empty"

    def readFile(self):
        with open(f"{self.name}.ndb", "r", encoding="utf8") as f:
            f.seek(0)
            if len(f.read()) > 0:
                f.seek(0)
                data = f.read()
                return data
            else:
                return "File is Empty"
