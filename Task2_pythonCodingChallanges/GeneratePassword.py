'''
Created on 31 May 2020

@author: poshan
'''
import random
import string

class GeneratePassword:
    def newPassword(self,length):
        alphaLetter = string.ascii_letters
        numericVal = string.digits
        specChar = string.punctuation
        nPassword = ''.join(random.choice(alphaLetter + specChar + numericVal) for i in range(length))
        print(nPassword)
            
        
myObj = GeneratePassword()
myObj.newPassword(15)