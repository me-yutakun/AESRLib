class fileHandler:

    f,liststr=open(file,'rb'),''
    for i in f.readlines():
        liststr+=i.decode()
    print(liststr)
    f.close()