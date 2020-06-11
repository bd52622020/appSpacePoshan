class FootBallTeam:
    tName = "Unkonwn "
    nWins = 0
    nLoss = 0
    nDraw = 0
    def teamName(self):
        self.tName = input("Enter the name of the Team: ")
        self.nWins = int(input("Enter the no of wins: "))
        self.nDraw = int(input("Enter the no of draw: "))
        self.nLoss = int(input("Enter the no of loss: "))
        
        self.totalPoints()
        
    def totalPoints(self):
        totalWinninfPoint = self.nWins * 3
        totalDrawPoint = self.nDraw * 1
        
        overallPoints = totalWinninfPoint + totalDrawPoint
         
        print("Win :" , totalWinninfPoint)
        print("Draw :" , totalDrawPoint)
        print("loss :", self.nLoss)
        print("overallPoints :" , overallPoints)
         
        tauntDict = {"Taunt1": "!! This team is not made for playing football !!",
                     "Taunt2": "You Suck"}
        BadDict = {"Bad Comments1": "!! This team is not doing their best !!",
                  "Bad Comments2": "The management of team is a failure"}
        
        GoodDict = {"Good Comments1": "!! Bravo, keep it up !!",
                  "Good Comments2": "Amazing Performance, this team is a legend"}
        
        if overallPoints >= 1000:
            if overallPoints >= 1200:
                comment = GoodDict.get("Good Comments1")
            else:
                comment = GoodDict.get("Good Comments1")
         
        elif overallPoints >= 700:  
            if overallPoints >= 900:
                comment = BadDict.get("bad Comments1")
            else:
                comment = BadDict.get("bad Comments1")
        else:
            comment = tauntDict.get("Taunt2")
            
        print(comment)

obj4 = FootBallTeam()
obj4.teamName()       
           