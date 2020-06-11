'''
Created on 8 Jun 2020

@author: poshan
'''
from _ast import In
class DictionaryList:
    
    def myDictionary(self):
        
       dict = {"name" : "Xavier"}
#         print(dict)
#         list_set = list(dict.values())
#         list_set.sort()
#         print(list_set)
       print(sorted(dict.values()))
    
    def myList(self):
        print("Test")
        
# Write a Python class which has two methods get_String and print_String.  
# 
# get_String accept a string from the user sa 
# 
# print_String print the string in upper case.

class LowerToUpper:
    inputVal = " "
    def get_String(self):
        self.inputVal = input("Enter text : " )
        self.print_String()
        
    def print_String(self):
        print(str.upper(self.inputVal))

#Write a Python program to check the validity of password input by users. Go to the editor 
import re
class PasswordValidator():
    
    inputVal = " "
    upperVal = 0
    lowerVal = 0
    numericVal = 0
    def get_String(self):
        self.inputVal = input("Enter password : " )
        self.checkPassword()
        
    def checkPassword(self):
        
        if(len(self.inputVal) < 6 and len(self.inputVal) > 12):
            print("Letter must be greater than 6  and less than 12 character")
            
        for i in self.inputVal:
             if (i.isupper()):
                 self.upperVal = 1
             elif(i.islower()):
                 self.lowerVal = 1   
             elif(i.isnumeric()):
                 self.numericVal = 1
                               
        
        if(self.upperVal == 0 and self.lowerVal == 0 and self.numericVal == 0  ):
            print("Letter must be Upper and Lower Case and have numeric digit")   
            
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')   
        if(regex.search(self.inputVal) == None): 
            print("Letter must contain special charater")
                 
        
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
    
       
obj1 = DictionaryList()
obj1.myDictionary()
obj2 = LowerToUpper()
obj2.get_String()
obj3 = PasswordValidator()
obj3.get_String()
obj4 = Pattern
obj4.myPattern()

 



