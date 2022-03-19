from .FileHandler import fileHandler
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto import Random
import binascii
import os

class KMI:
    def __init__(self):
        self.plength=32

    def StoB(self, s):
        return binascii.unhexlify(s)

    def BtoS(self, b):
        return str(binascii.hexlify(b))[2:-1]

    def getPrivateKey(self,password):
        salt = os.urandom(16)
        key = PBKDF2(password, salt, 64, 1000)
        return (key[:32],salt)
    
    def returnPKey(self, pwd, salt):
        key = PBKDF2(pwd, salt, 64, 1000)
        return key[:32]
        
    def createConf(self, pwd, file):
        ppass = self.getPrivateKey(pwd)
        iv=Random.new().read(AES.block_size)
        filelen=str(fileHandler.reader(fileHandler(), file)[1]).encode('utf-8')
        pKey=self.BtoS(ppass[1])+self.BtoS(iv)+self.BtoS(filelen)
        return (AES.new(ppass[0], AES.MODE_CBC, iv),pKey)

    def getConf(self, inpass, pKey):
        if(inpass is not None and pKey is not None):
            pwd=self.returnPKey(inpass, self.StoB(pKey[:self.plength]))
            iv=self.StoB(pKey[self.plength:2*self.plength])
            return AES.new(pwd, AES.MODE_CBC, iv)
        else:
            raise ValueError("You can't proceed without entering pKey/password!")