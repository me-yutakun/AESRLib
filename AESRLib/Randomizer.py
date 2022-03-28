import random
import base64
from .FileHandler import fileHandler
from .KMI import KMI
class Randomizer:
    def encrypt(self, file):
        alpha=KMI.createAlpha(KMI())
        rawList=fileHandler.readLines(file)[0]
        mapper = KMI.AlphaMap(KMI(), alpha)
        encList=rawList.copy()
        aKey = ''.join(arr)
        for i in range(0,len(rawList)):
            encList[i]=rawList.translate(rawList.maketrans(mapper))
        loc = random.randint(0, len(rawList) - 1)
        rawList.insert(loc, aKey)
        data=''.join(rawList)
        fileHandler.writer(fileHandler(), data, file)
        return aKey