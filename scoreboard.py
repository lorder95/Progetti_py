from CircularPositionalList import CircularPositionalList


class ScoreBoard:
    # ------------------------------- nested _Score class -------------------------------
    class _Score:

        def __init__(self, player, score, dataScore):
            self._namePlayer = player
            self._scorePlayer = score
            self._data = dataScore

        def __ge__(self, other):
            return self._scorePlayer >= other._scorePlayer

        def __eq__(self, other):
            return self._scorePlayer == other._scorePlayer and self._namePlayer == other._namePlayer and self._data == other._data

        def __ne__(self, other):
            return not (self == other)

        def __lt__(self, other):
            return self._scorePlayer < other._scorePlayer

        def __str__(self):
            return "Name Player:" + self._namePlayer +" Score:" + str(self._scorePlayer) +" Data:" + self._data + "\n"

    def __init__(self, x = 10):

        self._circList = CircularPositionalList()
        self._listCapacity = x

    def __len__(self):
        return self._listCapacity

    def size(self):
        return len(self._circList)

    def Is_empty(self):
        return self.size() == 0

    def insert(self, s):
        # First Case : The ScoreBoard is not full

        if self.Is_empty():
            self._circList.add_first(s)

        elif self.size() < self._listCapacity:

            if self.size() == 1:
                position = self._circList.first()
                if s < position.element():
                    self._circList.add_first(s)
                elif s > position.element():
                    self._circList.add_last(s)
                elif s == position.element():
                    raise Exception("Score già inserito")
                else:
                    self._circList.add_first(s)
            else:
                self._fillScoreBoard(s)

        elif self.size() == self._listCapacity:
            if s >= self._circList.first().element():
                if s != self._circList.first().element():
                    self._circList.delete(self._circList.first())
                    self._fillScoreBoard(s)

    def _fillScoreBoard(self, s):
        position = self._circList.first()

        while (s >= position.element()) and (position._node._next != self._circList._header._next):
            position = self._circList._after(position)

        print("position in uscita" + str(s))

        if s == position._node._prev._element:
            raise Exception("Score già inserito")

        if position == self._circList.last():
            if self.size() == len(self):
                self._circList.delete(self._circList.first())
            if s > position.element():
                self._circList.add_last(s)
            else:
                self._circList.add_before(position, s)

        else:
            ##Và fatto l'add after sia se s è maggiore che uguale a un elemento
            if self.size() == len(self):
                self._circList.delete(self._circList.first())
            self._circList.add_before(position, s)

    def top(self,i=1):
        if i > 0:
            if self.Is_empty():
                raise Exception("ScoreBoard Vuoto")
            else:

                if i > self.size():
                    i = self.size()
                position = self._circList.last()
                listaTop = []

                for k in range (i):
                    listaTop.append(position)
                    position = self._circList._before(position)

                return listaTop

        else:
            raise Exception("Indice non valido")

    def last(self,i=1):
        if i > 0:
            if self.Is_empty():
                raise Exception("ScoreBoard Vuoto")
            else:

                if i > self.size():
                    i = self.size()
                position = self._circList.first()
                listaTop = []

                for k in range (i):
                    listaTop.append(position)
                    position = self._circList._after(position)

                return listaTop

        else:
            raise Exception("Indice non valido")

    def merge(self,new):
        listMerged  = CircularPositionalList.merge(self._circList, new._circList)

        len1 = len(listMerged)
        #print("lunghezza listmerged: " + str(len1))

        if len1 > self._listCapacity:
            while len(listMerged) > self._listCapacity:
                position = listMerged.first()
                listMerged.delete(position)

        self._circList = listMerged

    def __str__(self):
        return "Scoreboard"+str(self._circList)






### ------ Test -------- ###

scoreBoard = ScoreBoard(3)

score1 = scoreBoard._Score("Marco", 230, "05/09/2018")
scoreBoard.insert(score1)

score2 = scoreBoard._Score("Peppe", 230, "05/09/2018")
scoreBoard.insert(score2)

score2 = scoreBoard._Score("Peppe", 230, "05/09/2018")
scoreBoard.insert(score2)

#score2 = scoreBoard._Score("Toni",280,"05/09/2018")
#scoreBoard.insert(score2)

score3 = scoreBoard._Score("Ludovica",250,"10/09/2018")
scoreBoard.insert(score3)

score4 = scoreBoard._Score("XXX",270,"10/09/2018")
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
#print(str(scoreBoard))

print("primo scoreboard: " + str(scoreBoard))

'''
lista=scoreBoard.top(2)
for e in lista:
    print(e.element())
lista=scoreBoard.last(2)
for e in lista:
    print(e.element())
'''

'''
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