import os
from typing import List
from sys import exit
class fileHandler:
    def isExistingFile(self, file: str) -> bool:
        if os.path.isfile(os.path.join(os.getcwd(), os.path.basename(file))):
            return True
        else:
            return False

    def reader(self, rfile: str) -> tuple[str,int]:
        try:
            if os.path.getsize(rfile) > 0:
                with open(rfile, "r",encoding="utf-8") as f:
                    data=f.read()
                    f.close()
            else:
                print('Provided file is empty!')
                exit(1)
        except IOError as e:
            print(e)
            exit(1)
        return (data,len(data))

    def writer(self, data: str, wfile: str):
        with open(os.path.basename(wfile),"w",encoding="utf-8") as f:
            f.write(data)
            f.close()

    def readLines(self, rfile: str) -> tuple[List[str],int]:
        try:
            if os.path.getsize(rfile) > 0:
                with open(rfile, "r",encoding="utf-8") as f:
                    data=f.readlines()
                    f.close()
            else:
                print('Provided file is empty!')
                exit(1)
        except IOError as e:
            print(e)
            exit(1)
        return (data,len(data))
