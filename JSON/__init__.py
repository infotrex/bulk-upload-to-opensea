import json

import os


class JSON:

    def __init__(self, filename):
        self.filename = filename

    def readFromFile(self):
        return json.load(open(file=self.filename))


if __name__ == '__main__':
    data = JSON(os.getcwd() + "/../data/metadata.json")
    print(data)
    data=data.readFromFile()
    for key in data:
        name = "#" + key
        description = name + " from DemonQueenNFT"
        file = key + ".png"
        metadata = data[key]
        print(name, description, file, metadata)