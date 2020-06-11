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
            print("Password must be Upper and Lower Case and have numeric digit")   
            
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')   
        if(regex.search(self.inputVal) == None): 
            print("Password must contain special character")
            
obj3 = PasswordValidator()
obj3.get_String()