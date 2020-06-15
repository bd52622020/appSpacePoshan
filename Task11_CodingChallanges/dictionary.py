
# Given dictionary is consisted of vehicles and their weights in kilograms. 
#Construct a list of the names of vehicles with weight below 5000 kilograms. 
#In the same list comprehension make the key names all upper case.

class Dict:
    
    def dictList(self):
        oldDict = {"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "semi": 13600, "Bicycle":7, "motorcycle": 110}
        
        # convert key names to upper case
        
        upperCaseDict =  {k.upper(): v for k, v in oldDict.items()}
        
        # empty dict
        newDict = dict()
        
        #iterating in loop
        
        for(key, value) in upperCaseDict.items():
            if value < 5000:
                newDict[key] = value
                
        print(upperCaseDict)
        print(newDict)

obj = Dict()
obj.dictList()


        
        