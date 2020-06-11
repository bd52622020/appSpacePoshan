# print_String print the string in upper case.

class LowerToUpper:
    inputVal = " "
    def get_String(self):
        self.inputVal = input("Enter text : " )
        self.print_String()
        
    def print_String(self):
        print(str.upper(self.inputVal))

obj2 = LowerToUpper()
obj2.get_String()