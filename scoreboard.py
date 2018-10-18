from CircularPositionalList import CircularPositionalList


class ScoreBoard:
    # ------------------------------- nested _Score class -------------------------------
    class _Score:

        def __init__(self, player, score, dataScore):
            self._namePlayer = player
            self._scorePlayer = score
            self._data = dataScore

        def __gt__(self, other):
            return self._scorePlayer > other._scorePlayer

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
        # First Case : The ScoreBoard is empty
        if self.Is_empty():
            self._circList.add_first(s)

        # Second Case : The ScoreBoard is not full
        elif self.size() < self._listCapacity:

            # Subcase of the Second Case: The ScoreBoard has only one Score
            if self.size() == 1:
                position = self._circList.first()

                if s < position.element():
                    self._circList.add_first(s)

                elif s > position.element():
                    self._circList.add_last(s)

                elif s == position.element():
                    raise Exception("Score già presente")

                else:
                    self._circList.add_first(s)
            else:
                self._fillScoreBoard(s, False)

        # Third and last case: The ScoreBoard is full
        elif self.size() == self._listCapacity:
            if s > self._circList.first().element():
                self._fillScoreBoard(s, True)
            elif s == self._circList.first().element():
                raise Exception("Score già inserito")
            else:
                raise Exception("Score non abbastanza alto")

    #Private method that insert the Score inside the ScoreBoard in the right position.
    #IL parametro bool mi serve perchè a priori non posso cancellare un elemento. Se ad es. lo score già è presente poi non avrei il modo di ripristinare
    #lo score cancellato.
    def _fillScoreBoard(self, s ,bool):
        position = self._circList.first()

        while (s >= position.element()) and (position._node._next != self._circList._header._next):
            position = self._circList._after(position)

        #Particul Case
        if position == self._circList.last():

            if s == position.element():
                raise Exception("Score già inserito")

            #Handle possible delete
            if bool == True:
                self._circList.delete(self._circList.first())
            if s > position.element():
                self._circList.add_last(s)
            else:
                self._circList.add_before(position, s)

        else:
            #Case score yet insered
            if s == position._node._prev._element:
                raise Exception("Score già presente")
            #Handle possible delete
            if bool == True:
                self._circList.delete(self._circList.first())

            self._circList.add_before(position, s)

    ##Sarebbe meglio se la lista restituita contenesse _Score anziché position
    def top(self, i = 1):
        if i > 0:
            if self.Is_empty():
                raise Exception("ScoreBoard vuoto")
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
            raise Exception("Parametro non valido")

    ##Sarebbe meglio se la lista restituita contenesse _Score anziché position
    def last(self, i = 1):
        if i > 0:
            if self.Is_empty():
                raise Exception("ScoreBoard vuoto")
            else:
                if i > self.size():
                    i = self.size()
                position = self._circList.first()
                listaLast = []

                for k in range (i):
                    listaLast.append(position)
                    position = self._circList._after(position)

                return listaLast

        else:
            raise Exception("Parametro non valido")

    def merge(self, new):
        listMerged  = CircularPositionalList.merge(self._circList, new._circList)

        len1 = len(listMerged)

        if len1 > self._listCapacity:
            # Cancello _Score in eccesso dalle prime posizioni fino a raggiungere la dimensione corretta
            while len(listMerged) > self._listCapacity:
                position = listMerged.first()
                listMerged.delete(position)

        self._circList = listMerged

    def __str__(self):
        return "Scoreboard" + str(self._circList)