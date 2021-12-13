import csv
import os
from typing import TextIO


class CSV:

    def __init__(self, filename):
        self.filename = filename

    def readFromFile(self):
        with open(self.filename) as fileIO:
            data = []
            for row in csv.DictReader(fileIO):
                data.append(row)
            return data



