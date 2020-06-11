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
           
class FindLepYear:
    
    def getYear(self):
        year = int(input("Enter the year : " ))
        if (year % 4) == 0:
            print(year, " is a leap Year")
        else:
            print(year, "is not a leap year")


class NumberVerification:
     def getISBN(self):
        ISBN = "3-598-21508-8"
        ISBN = ISBN.replace("-","")
        if len(ISBN)==10:
            print("The no is valid")
        else:
            print("The no is invalid")
        
       
    


class GetNumbers:
    
    def getNo(self):
         
         myList = [2,3,5,8,1,2]
         firstNo = myList[0]
         lastNo = myList[-1]
         
         if firstNo == lastNo:
             print("Numbers are equals")
         else:
             print("Numbers are not equals")
         
         

        
obj = MyPrimeNo()
obj.findPrimeNo()
 
obj2 = FindLepYear()
obj2.getYear()

obj3 = NumberVerification()
obj3.getISBN()

obj4 = GetNumbers()
obj4.getNo()


