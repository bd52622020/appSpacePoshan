class Task1:
    input1 = ""
    input2 = ""
    
    def askInput(self):
        self.input1 = input("Your first input")
        self.input2 = input("Second Input")
        
    def saveInputs(self):
        f = open("myfile.txt", "a")
        f.write(self.input1 + " " + self.input2 + " ")
        f.close()
        print("Your Text has been saved sucessfully")
        
myObj = Task1()
myObj.askInput()
myObj.saveInputs()
        
