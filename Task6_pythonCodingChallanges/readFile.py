import os
class ReadFile():
    
    def fileRead(self):
        try:
            filesize = os.path.getsize("demo.txt")
            if filesize == 0:
                print("The file is empty : " + str(filesize))
            else:
                print("This file contains some information : " + str(filesize))
                        
            f = open("demofile.txt", "r")
            print(f.read(10))
        except:
            print("The File Does not Exist")
    
obj2 = ReadFile()
obj2.fileRead()     