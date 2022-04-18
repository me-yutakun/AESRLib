import AESRLib as ar

print("### WELCOME TO AESRandomizer1.0 ###")
print("We support only file input as of now, string support to be added in future.")
ip=input("Pls enter filename/string for encryption/decryption:")
ar.AESRandomizer.initializer(ip)