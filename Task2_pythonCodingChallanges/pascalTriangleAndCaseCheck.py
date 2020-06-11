
class Task:
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
       
    def pascalTriangel(self):
        n = int(input("Enter number of rows: "))
        a=[]
        for i in range(n):
            a.append([])
            a[i].append(1)
            for j in range(1,i):
                a[i].append(a[i-1][j-1]+a[i-1][j])
            if(n!=0):
                a[i].append(1)
        for i in range(n):
            print("   "*(n-i),end=" ",sep=" ")
            for j in range(0,i+1):
                print('{0:6}'.format(a[i][j]),end=" ",sep=" ")
            print()     
    
myObj = Task()
myObj.getInput()   
myObj.pascalTriangel()         
            
        
    