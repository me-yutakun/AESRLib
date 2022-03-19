class fileHandler:
    def reader(self,rfile):
        with open(rfile, "r") as f:
            data=f.read()
            f.close()
        return (data,len(data))
    def writer(self, data, wfile):
        with open(wfile,"w") as f:
            f.write(data)
            f.close()
