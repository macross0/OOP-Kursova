import os, glob
from typing_extensions import Self
from uuid import uuid4
import itertools

path = '/database'
machineries = []

class Machinery():
    def __init__(self, name, type, status, history, filename = None):
        self.name = str(name).replace('\n', '')
        self.type = str(type).replace('\n', '')
        self.status = str(status).replace('\n', '')
        self.history = history

        if (filename) == None:
            self.filename = str(uuid4() + '.data')
        else:
            self.filename = str(filename)

    def getFileName():
        return os.path.join(os.getcwd(), '/database', Self.filename)

def readDatabase():
    global machineries
    global path

    for filename in glob.glob(os.path.join(path, '*.data')):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            data = f.readlines()
            history = {}

            for date, message in zip(data[3::2], data[4::2]):
                date.replace('\n', '')
                message.replace('\n', '')
                history[date] = message

            machineries.append(Machinery(data[0], data[1], data[2], history))

def writeToDatabase():
    global machineries
    global path

    for entry in machineries:
        with open(entry.getFileName(), 'w') as f:
            _buffer = [entry.name, entry.type, entry.status, entry.history]
            buffer = itertools.chain(*_buffer)
            f.writelines(buffer)

readDatabase()
print(machineries[0].history)
