import base64
from .KMI import KMI
class AESEncrypter:
    def __init__(self):
        self.PAD_SIZE=16

    def pad(self,s):
        s+= (self.PAD_SIZE - len(s) % self.PAD_SIZE) * chr(self.PAD_SIZE - len(s) % self.PAD_SIZE)
        return s

    def unpad(self,s):
        s+=s[:-ord(s[len(s) - 1])]
        return s

    def encrypt(self,raw,conf):
        return conf.encrypt(self.pad(raw).encode())

    def decrypt(self,ciphertext,conf):
        return self.unpad(conf.decrypt(ciphertext).decode())

def initializer(file):
    choice = input("Do you want to create a new key or proceed with existing key: [y/n]")
    match choice.lower():
        case 'y':
            password = input("ENCRYPTION: Please enter a new password:")
            conf= KMI.createConf(KMI(), password)
            enc=AESEncrypter.encrypt(AESEncrypter(), file, conf[0])
            print("Your pKey is: {}".format(conf[1]))
            print("enc: {}".format(enc))
        case 'n':
            try:
                pKey=input("DECRYPTION: Please enter your pKey:")
                print(AESEncrypter.decrypt(AESEncrypter(), file, KMI.getConf(KMI(),pKey)))
            except Exception as e:
                print(e)
        case _:
            raise ValueError("Please enter valid input!")
