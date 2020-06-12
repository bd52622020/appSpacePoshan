'''
Created on Jun 12, 2020

@author: Poshan

'''
class Lambda1:
    
    def useLambdaFunctions(self):
        
        x = lambda givenNo : givenNo + 15 
        
        y = lambda a,b : a * b
        
        print(x(10))
        print(y(10,20))
        
obj = Lambda1()
obj.useLambdaFunctions()