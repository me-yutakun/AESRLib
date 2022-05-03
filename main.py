import AESRLib as ar

print("### WELCOME TO AESRandomizer1.0 ###")
print("We support only file input as of now, string support to be added in future.")
ip=input("Pls enter filename for encryption/decryption:")
ar.AESRandomizer.initializer(ip)
input("Please enter any key to exit...\n")