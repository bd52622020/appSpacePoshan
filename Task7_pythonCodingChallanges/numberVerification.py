class NumberVerification:
     def getISBN(self):
        ISBN = "3-598-21508-8"
        ISBN = ISBN.replace("-","")
        if len(ISBN)==10:
            print("The no is valid")
        else:
            print("The no is invalid")
            
obj3 = NumberVerification()
obj3.getISBN()