'''
Created on Jun 10, 2020

@author: Poshan
'''
class MyPrimeNo:
    
    def findPrimeNo(self):
        num = int(input("Enter the prime no : " ))
        if num > 1:
       # check for factors
            for i in range(2,num):
                if (num % i) == 0:
                   print(num,"is not a prime number")
                   print(i,"times",num//i,"is",num)
                 
                else:
                   print(num,"is a prime number")
        else:
           print(num,"is not a prime number")
           
obj = MyPrimeNo()
obj.findPrimeNo()