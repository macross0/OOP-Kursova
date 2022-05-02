from email import message
import os, glob

machineries = []

class Machinery():
    def __init__(self, name, type, status, history):
        self.name = str(name).replace('\n', '')
        self.type = str(type).replace('\n', '')
        self.status = str(status).replace('\n', '')
        self.history = history

def readDatabase():
    global machineries

    path = 'database'

    for filename in glob.glob(os.path.join(path, '*.data')):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            data = f.readlines()
            history = {}

            for date, message in zip(data[3::2], data[4::2]):
                date.replace('\n', '')
                message.replace('\n', '')
                history[date] = message

            machineries.append(Machinery(data[0], data[1], data[2], history))

readDatabase()
print(machineries[0].history)
