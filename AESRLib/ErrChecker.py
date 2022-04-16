import os
class ErrorScan:
    def nTry(self,ismodify):
        if not os.path.exists('nt'):
            f=open('nt','x')
            f.close()

        with open('nt', 'r') as f:
            erc = f.read(1)
            f.close()

        if (erc == '' or erc is None):
            erc=0

        erc=int(erc)
        if(ismodify):
            with open('nt','w') as f:
                f.write(str(erc + 1))
                f.close()
        return erc

class FaultCheck:
    def faultTest(self):
        return False