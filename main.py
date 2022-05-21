import AESRLib as ar

if __name__=="__main__":
    ip=input("Pls enter filename for encryption/decryption:")
    ar.AESRandomizer.initializer(ip)
    input("Press enter to exit...")