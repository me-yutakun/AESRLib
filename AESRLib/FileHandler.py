import os
class fileHandler:
    def isFile(self, file):
        try:
            if(os.path.isfile(os.path.join(os.getcwd(), os.path.basename(file)))):
                return True
            else:
                return False
        except:
            return False

    def reader(self, rfile):
        try:
            if os.path.exists(rfile):
                with open(rfile, "r") as f:
                    data=f.read()
                    f.close()
        except IOError as e:
            print(e)
        return (data,len(data))

    def writer(self, data, wfile):
        with open(wfile,"w") as f:
            f.write(data)
            f.close()

    def readLines(self, rfile):
        with open(rfile, "r") as f:
            data=f.readlines()
            f.close()
        return (data,len(data))