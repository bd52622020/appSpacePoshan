# Create a dictionary (in your file) of names and birthdays. 
# When you run your program it should ask the user to enter a name, 
# and return the birthday of that person back to them. 
# The interaction should look something like this:


class DictionList:
    def myList(self, cName):
        birthDayList = {"John": "2nd June",
                        "Sophiya": "5th Aug",
                         "Ida": "10th Dec",
                         "Nelson": "13th Dec",
                         "Brat": "1st Jan",
                         "Chrish": "3rd April",
                         "Jackie": "23nd Nov",
                         "Mike": "2nd Oct",
                         }
        
        if birthDayList.get(cName): 
            print ("DOB of cName is :", birthDayList[cName]) 
        else: 
            print ("Records not Available")




class Interaction(DictionList):
    
    def checkName(self):
        cName = input("Enter your name : ")
        
        
        searchValue = DictionList.myList(self,cName)
        
obj = Interaction()
obj.checkName()
            
        
        