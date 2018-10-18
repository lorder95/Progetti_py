from scoreboard import ScoreBoard

scoreBoard = ScoreBoard(3)

score1 = scoreBoard._Score("Marco", 220, "05/09/2018")
scoreBoard.insert(score1)

score2 = scoreBoard._Score("Peppe", 300, "05/09/2018")
scoreBoard.insert(score2)

score3 = scoreBoard._Score("Paolo", 150, "05/09/2018")
scoreBoard.insert(score3)

# Lo ScoreBoard è adesso pieno

#score2 = scoreBoard._Score("Toni",280,"05/09/2018")
#scoreBoard.insert(score2)

score3 = scoreBoard._Score("Ludovica",218,"10/09/2018")
scoreBoard.insert(score3)

score4 = scoreBoard._Score("XXX",189,"10/09/2018")
scoreBoard.insert(score4)

#score5 = scoreBoard._Score("Revenger",280,"10/09/2018")
#scoreBoard.insert(score5)

##Questa insert è importante perchè ci mostra che un elemento viene aggiunto nello scoreboard solo se è maggiore del più piccolo già presente
#score6 = scoreBoard._Score("XXY",250,"10/09/2018")
#scoreBoard.insert(score6)

score7 = scoreBoard._Score("ABC",300,"10/09/2018")
#scoreBoard.insert(score7)
#print(str(scoreBoard))

score8 = scoreBoard._Score("DFE",250,"10/09/2018")
#scoreBoard.insert(score8)

print(str(scoreBoard))

'''
lista=scoreBoard.top(2)
for e in lista:
    print(e.element())
lista=scoreBoard.last(2)
for e in lista:
    print(e.element())


scoreBoard2 = ScoreBoard(5)
score10 = scoreBoard2._Score("Gesù",1000,"10/09/2018")
scoreBoard2.insert(score10)

score11 = scoreBoard2._Score("Giuseppe",1010,"10/09/2018")
scoreBoard2.insert(score11)

score12 = scoreBoard2._Score("Pasquale",1050,"10/09/2018")
scoreBoard2.insert(score12)

score13 = scoreBoard2._Score("Francesco",1200,"10/09/2018")
scoreBoard2.insert(score13)

score14 = scoreBoard2._Score("Maria",1060,"10/09/2018")
scoreBoard2.insert(score14)
print("ScoreBoard")
print(scoreBoard2)


score15 = scoreBoard2._Score("Dio",6070594,"10/09/2018")
scoreBoard2.insert(score15)

scoreBoard.merge(scoreBoard2)
print("merged: " + str(scoreBoard))
'''