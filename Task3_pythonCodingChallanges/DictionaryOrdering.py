class DictionaryList:
    
    def myDictionary(self):
        
       dict = {"name" : {"Xavier", "Test1", "Test3", "Test2"}}
       list1 = list(dict.values())
       print(sorted(list1, key=None, reverse=False))
      
      
            
    
obj1 = DictionaryList()
obj1.myDictionary()