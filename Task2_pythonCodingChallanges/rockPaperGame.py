'''
Created on 29 May 2020

@author: poshan
'''

class MyClass:
    player1 = ""
    player1 = ""
    
    def results(self):
         if(self.player1 == "ROCK" and self.player2 == "ROCK"):
             print("Draw")
         elif(self.player1 == "ROCK" and self.player2 == "PAPER"):
                 print("Player2 wins")
         elif(self.player1 == "ROCK" and self.player2 == "SCISSORS"):
                 print("Player1 Wins")
         elif(self.player1 == "PAPER" and self.player2 == "ROCK"):
                 print("Player1 wins")
         elif(self.player1 == "PAPER" and self.player2 == "PAPER"):
                 print("Draw")
         elif(self.player1 == "PAPER" and self.player2 == "SCISSORS"):
                 print("Player2 wins")
         elif(self.player1 == "SCISSORS" and self.player2 == "ROCK"):
                 print("Player2 wins")
         elif(self.player1 == "SCISSORS" and self.player2 == "PAPER"):
                 print("player1")
         elif(self.player1 == "SCISSORS" and self.player2 == "SCISSORS"):
                 print("Draw")
         else:
                print("No winners")
                
         print("Play again")
         self.inputs()
       
    def inputs(self):
       self.player1 = input("player1:").upper()
       self.player2= input("player2:").upper()
       self.results()
        
        
    
a = MyClass()
a.inputs()
      
        
        
        