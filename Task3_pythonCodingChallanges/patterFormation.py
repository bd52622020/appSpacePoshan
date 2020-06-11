class Pattern:
    
    def myPattern(x = 5):
        for i in range(x):
            for j in range(i):
                print("*", end="")
            print()
        for i in range(x):
            for j in range(x-i):
                print("*", end="")
            print() 
            
obj4 = Pattern
obj4.myPattern()