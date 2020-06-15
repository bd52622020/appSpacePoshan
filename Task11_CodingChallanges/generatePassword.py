# Write a password generator in Python. 
# Be creative with how you generate passwords - strong passwords have a mix of 
# lowercase letters, uppercase letters, numbers, and symbols. 
# The passwords should be random, generating a new password every time the user asks for a new password. 
# Include your code in a main method.

import random
import string

class GeneratePassword:
    def newPassword(self):
        passwordLength = 15
        alphaLetter = string.ascii_letters
        numericVal = string.digits
        specChar = string.punctuation
        nPassword = ''.join(random.choice(alphaLetter + specChar + numericVal) for i in range(passwordLength))
        print(nPassword)
        
            
       
myObj = GeneratePassword()
myObj.newPassword()