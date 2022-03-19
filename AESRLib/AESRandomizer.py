import base64
from .KMI import KMI
from .FileHandler import fileHandler
from .ErrChecker import ErrorScan, FaultCheck
class AESEncrypter:
    def __init__(self):
        self.PAD_SIZE=16

    def pad(self,s):
        s+= (self.PAD_SIZE - len(s) % self.PAD_SIZE) * chr(self.PAD_SIZE - len(s) % self.PAD_SIZE)
        return s

    def unpad(self,s):
        s+=s[:-ord(s[len(s) - 1])]
        return s

    def AESencrypt(self,raw,conf):
        return conf.encrypt(self.pad(raw).encode('utf-8'))

    def AESdecrypt(self,ciphertext,conf):
        return self.unpad(conf.decrypt(ciphertext).decode('utf-8'))

def initializer(file):
    if(ErrorScan.nTry(ErrorScan(), None)<3):
        choice = input("Do you want to create a new key or proceed with existing key: [y/n]")
        match choice.lower():
            case 'y':
                print("<--- ENCRYPTION INTERFACE -->")
                flag=True
                while(flag):
                    print("Executing Phase 1/2 Encryption")
                    pwd = input("Please enter a new password:")
                    conf = KMI.createConf(KMI(), pwd, file)
                    enc = AESEncrypter.AESencrypt(AESEncrypter(), fileHandler.reader(fileHandler(), file)[0], conf[0])
                    enc = KMI.BtoS(KMI(), enc)
                    print("Started automated fault check [beta]...")
                    flag = FaultCheck.faultTest(FaultCheck())
                    if(flag):
                        print("Fault found in pKey, please re-create your key again!")
                print("Completed fault check: No issues found.")
                print("Note: This pkey below will be shown only once! Please keep it safe and remember the password that you entered before!")
                print("Your pKey is: {}".format(conf[1]))
                print("Completed Phase 1/2...Starting Phase 2/2 Encryption")
                fileHandler.writer(fileHandler(), enc, file)
            case 'n':
                try:
                    print("<-- DECRYPTION INTERFACE -->")
                    pKey=input("Please enter your pKey:")
                    print("Note: For every wrong password, you will get wrong decrypted data and max 3 attempts are allowed! Its case sensitive.")
                    pwd = input("Please enter your password to proceed:")
                    conf= KMI.getConf(KMI(), pwd, pKey)
                    bdec=KMI.StoB(KMI(), fileHandler.reader(fileHandler(), file)[0])
                    dec=AESEncrypter.AESdecrypt(AESEncrypter(), bdec, conf)[:int(KMI().StoB(pKey[2*KMI().plength:len(pKey)]).decode('utf-8'))]
                    fileHandler.writer(fileHandler(), dec, file)
                except UnicodeDecodeError as e:
                    ErrorScan.nTry(ErrorScan(), True)
                    print("You entered wrong password!")
                except Exception as e:
                    print(e)
            case _:
                raise ValueError("Please enter valid input!")
    else:
        print("You exceeded max attempts!")
        exit(1)