from Crypto.Protocol.KDF import PBKDF2
from Crypto.Cipher import AES
from Crypto import Random
import binascii

class KMI:
    def __init__(self):
        self.plength=64

    def StoB(self,s):
        return binascii.unhexlify(s)

    def BtoS(self,b):
        return str(binascii.hexlify(b))[2:-1]

    def getPrivateKey(self,password):
        salt = os.urandom(16)
        key = PBKDF2(password, salt, 64, 1000)
        return key[:32]

    def createConf(self,pwd):
        ppass = self.getPrivateKey(pwd)
        iv = Random.new().read(AES.block_size)
        conf = AES.new(ppass, AES.MODE_CBC, iv)
        pk=self.BtoS(ppass)+self.BtoS(iv)
        return (conf,pk)

    def getConf(self,pKey):
        if(pKey is not None):
            return AES.new(self.StoB(pKey[:self.plength]), AES.MODE_CBC, self.StoB(pKey[self.plength:]))
        else:
            raise ValueError("You can't proceed without entering key!")
