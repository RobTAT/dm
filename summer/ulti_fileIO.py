__author__ = 'yuafan'

import pickle


def savePickle(dir_, stuff):
    with open(dir_ + 'DataPack.pickle', 'wb') as handle:
        pickle.dump(stuff, handle)


def loadPickle(dir_):
    return pickle.load(open(dir_ + 'DataPack.pickle',  "rb"))


