import os
class fileHandler:
    def reader(self, rfile):
        try:
            if os.path.exists(rfile):
                with open(rfile, "r") as f:
                    data=f.read()
                    f.close()
            else:
                with open(rfile, "x") as f:
                    f.close()
                reader(rfile)
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