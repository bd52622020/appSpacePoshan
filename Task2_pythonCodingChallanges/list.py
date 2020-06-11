'''
Created on 29 May 2020

@author: poshan
'''
class MyListOperations:
    myList = []
    
    def removeDuplicate(self):
        newList = list(dict.fromkeys(self.myList))
        print(newList)
        
    def listName(self):
        self.myList = ["Apple", "Banana", "Orange", "Grapes", "Pineapple", "Apple", "Banana", "Orange", "Grapes", "Pineapple"]
        print(self.myList)
        self.removeDuplicate()
    
    def loopList(self):
        loopList = []
        for i in self.myList:
            if(i not in loopList):
                loopList.append(i)
            
        print(loopList)

myObj = MyListOperations()
myObj.listName()
myObj.loopList()    