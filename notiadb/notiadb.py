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
