
class UpperAndLowerCase:
    countUpper = 0
    countLower = 0
    def getInput(self):
        inputVal = input("Input String Containing Uppercase and Lower Case :")
        self.inputValue = inputVal
        self.Calculate(inputVal)
        
    def Calculate(self,inputVal):
       for element in range(0, len(inputVal)):
           if(inputVal[element].isupper()):
               self.countUpper += 1
               
           elif(inputVal[element].islower()):
               self.countLower += 1
               
       print("Total Upper Char:", self.countUpper) 
       print("Total Lower Char:", self.countLower) 
        
myObj = UpperAndLowerCase()
myObj.getInput() 