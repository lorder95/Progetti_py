from scoreboard import ScoreBoard
#CREO PRIMO SCOREBOARD ORDINATO
scoreBoard = ScoreBoard(3)
score1 = scoreBoard._Score("Marco", 230, "05/09/2018")
scoreBoard.insert(score1)
score2 = scoreBoard._Score("Peppe", 230, "05/09/2018")
scoreBoard.insert(score2)
score3 = scoreBoard._Score("Paolo", 230, "05/09/2018")
scoreBoard.insert(score3)
print("Primo Scoreboard: \n" + str(scoreBoard))

#CREO SECONDO SCOREBOARD ORDINATO
scoreBoard2 = ScoreBoard(5)
score10 = scoreBoard2._Score("Nicola",1000,"10/09/2018")
scoreBoard2.insert(score10)
score11 = scoreBoard2._Score("Giuseppe",1010,"10/09/2018")
scoreBoard2.insert(score11)
score12 = scoreBoard2._Score("Pasquale",1050,"10/09/2018")
scoreBoard2.insert(score12)
score13 = scoreBoard2._Score("Francesco",1200,"10/09/2018")
scoreBoard2.insert(score13)
score14 = scoreBoard2._Score("Maria",1060,"10/09/2018")
scoreBoard2.insert(score14)
score15 = scoreBoard2._Score("Giovanni",6070594,"10/09/2018")
scoreBoard2.insert(score15)
print("Secondo Scoreboard")
print(scoreBoard2)

# MERGE DEI DUE SCOREBOARD (INPLACE)
scoreBoard.merge(scoreBoard2)
print("*****MERGED SCOREBOARD: \n" + str(scoreBoard))

