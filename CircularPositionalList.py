from TdP_collections.list.positional_list import PositionalList

class CircularPositionalList(PositionalList):



    def Is_sorted(self):

        for elem in self:
            if(self._validate(elem)._element<self._validate(elem)._next._element):
                return False

        return True

    def add_after(self, p, e):

        node = self._validate(p)


        if(node._next == self._header._next): # Quando aggiungiamo in coda occorre fare un insert_between tra primo e ultimo


            return self.add_last(e)

        else: return super().add_after(p,e)

    def add_before(self, p, e):

        node = self._validate(p)


        if(node._prev == self._trailer._prev): # Quando aggiungiamo in coda occorre fare un insert_between tra primo e ultimo


            return self.add_first(e)

        else: return super().add_before(p,e)

    #METODO PRIVATO UTILIZZATO PER FACILITARE  CONTAINS
    def _findpos(self,pos):
      #  if(e is None): raise Exception("E non è un elemento ")

        for posiz in self:
            if(posiz == pos):
                return posiz

        return None

    def find(self,e):
      #  if(e is None): raise Exception("E non è un elemento ")

        for elem in self:
            if(elem._node._element == e):
                return elem

        return None

    def clear(self):
        cursor = self.first()

        while cursor._node._next is not cursor._node: # Non posso usare header-> next poichè ad ogni passo cancello un elemento

            #print(cursor.element())
            app = cursor._node._next
            self.delete(cursor)
            cursor = self._make_position(app)


        self.delete(self.last())




    def count(self,e):
        cont=0
        for pos in self:
            if(pos._node._element==e):
                cont+=1
        return cont

    def reverse(self):
        lista_appoggio = []

        for pos in self :
            lista_appoggio.append(pos._node._element)

        for pos in self:
            pos._node._element = lista_appoggio.pop()



    def copy(self):

        new_list = CircularPositionalList()

        for pos in self:
            new_list.add_last(pos._node._element)

        return new_list


    def __iter__(self):
        cursor = self.first()
        while cursor._node._next is not self._header._next:
            yield cursor
            cursor = self.after(cursor)
        yield  cursor

    def add_last(self,e):

        node = self._trailer._prev

        if(self.is_empty()):


            new_node =  self._Node(e, None, None)
            new_node._prev = new_node
            new_node._next = new_node

            self._trailer._prev = new_node
            self._header._next = new_node
            self._size +=1
            return self._make_position(new_node)


        else:

            new_pos = self._insert_between(e, node,self._header._next)
            self._trailer._prev = new_pos._node


            return new_pos

    def add_first(self, e):

        node = self._header._next

        if(self.is_empty()):


            new_node =  self._Node(e, None, None)
            new_node._prev = new_node
            new_node._next = new_node

            self._trailer._prev = new_node
            self._header._next = new_node
            self._size +=1
            return self._make_position(new_node)


        else:

            new_pos = self._insert_between(e,self._trailer._prev,node)
            self._header._next = new_pos._node


            return new_pos


    def delete(self, p):
        original = self._validate(p)

        if(p==self.first()):
            self._header._next = p._node._next # L'header punta all'elemento dopo il primo
            self.last()._node._next = p._node._next # L'ultimo elemento della lista puta all'elem dopo il primo
        elif(p==self.last()):
            self._trailer._prev = p._node._prev # Trailer punterà il nodo che precede l'ultimo
            p._node._prev._next = p._node._next # Il campo next dell'ultimo nodo prima di quello elminato punterà al next del vecchio elem( punterà al primo della lista)

        return self._delete_node(original)  # inherited method returns element

    def __add__(self, other):

        new_list = self.copy()
        for pos in other:
            new_list.add_last(pos.element())
        return new_list

    def __contains__(self, position):
        self._validate(position)

        return self._findpos(position) is not None  # DA VERIFICARE

    def __len__(self):
        return self._size


    def __setitem__(self, pos, value):
        self._validate(pos)
        self.replace(pos,value)

    def __getitem__(self, pos):
        self._validate(pos)
        for posiz in self:
            if(posiz==pos):
                return posiz.element()

        raise Exception("Elemento non presente")

    def __delitem__(self,p):
            self._validate(p)
            self.delete(p)

    def __str__(self):
        lista =""
        if(not self.is_empty()):
            lista ="Lista=["

            for pos in self:
                if(pos!=self.last()):

                    lista += str(pos.element())
                    lista+=","
                else :

                    lista+=str(pos.element())

            lista+="]"

        else: print("LISTA VUOTA")

        return lista

    def merge(self,lista2):
        #Supponiamo le liste ordinate senza effettuare esplicitamente un controllo

        if(self.last().element()<lista2.first().element()): # casi di liste consecutive
            return self+lista2
        if(lista2.last().element()<self.first().element()): #
            return lista2+self

        new_list = self.copy()
        cursor = new_list.first()

        for pos in lista2:
            while(pos.element()>cursor.element() and cursor._node._next is not new_list._header._next):

                cursor = new_list.after(cursor)

            if(pos.element()<cursor.element()):
                new_list.add_before(cursor,pos.element())
            else:
                new_list.add_after(cursor,pos.element())

        return new_list

    def bubblesorted(self):
        lungh = self._size-1
        swap = True
        lista = self.copy()

        while(lungh>0 and swap):
            swap = False
            pos = lista.first()
            for pos in lista:

                if(pos.element()>lista.after(pos).element() and  pos != lista.last()):
                    swap = True
                    app = pos.element()
                    pos._node._element= pos._node._next._element
                    pos._node._next._element = app

            lungh-=1

        for pos in lista:
            yield pos.element()































































