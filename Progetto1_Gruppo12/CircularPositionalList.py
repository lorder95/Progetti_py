from TdP_collections.list.positional_list import PositionalList

class CircularPositionalList(PositionalList):


    def _before(self, p):
        if self._size==1:
            return None
        else:
            return super().before(p)

    def _after(self, p):
        if self._size==1:
            return None
        else:
            return super().after(p)

    def after(self, p): #Fa il controllo sulla dimensione. Altrimenti richiama after di PositionalList
        return self._after(p).element()

    def before(self, p): #Fa il controllo sulla dimensione. Altrimenti richiama before di PositionalList
        return self._before(p).element()

    def Is_empty(self):
        return super().is_empty()

    def Is_sorted(self):

        for pos in self._iter():
            if(self._validate(pos)._element > self._validate(pos)._next._element and self._validate(pos)._next != self._header._next):
                return False

        return True

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





    def find(self, e):
        if(e is None):
            raise ValueError("E non è un elemento")

        for pos in self._iter():
            if(pos._node._element == e):
                return pos

        return None

    def delete(self, p):
        original = self._validate(p)

        if(p==self.first()):
            self._header._next = p._node._next # L'header punta all'elemento dopo il primo
            self.last()._node._next = p._node._next # L'ultimo elemento della lista puta all'elem dopo il primo
        elif(p==self.last()):
            self._trailer._prev = p._node._prev # Trailer punterà il nodo che precede l'ultimo
            p._node._prev._next = p._node._next # Il campo next dell'ultimo nodo prima di quello elminato punterà al next del vecchio elem( punterà al primo della lista)

        return self._delete_node(original)  # inherited method returns element


    def clear(self):
        cursor = self.first()

        while cursor._node._next is not cursor._node: # Non posso usare header-> next poichè ad ogni passo cancello un elemento

            #print(cursor.element())
            app = cursor._node._next
            self.delete(cursor)
            cursor = self._make_position(app)


        self.delete(self.last())




    def count(self, e):
        cont=0
        for pos in self._iter():
            if(pos._node._element==e):
                cont+=1
        return cont

    def reverse(self):
        lista_appoggio = []

        for pos in self._iter():
            lista_appoggio.append(pos._node._element)

        for pos in self._iter():
            pos._node._element = lista_appoggio.pop()

    def copy(self):
        new_list = CircularPositionalList()

        for pos in self._iter():
            new_list.add_last(pos._node._element)

        return new_list

    def _iter(self): # iteratore privato sulle position
        cursor = self.first()
        while cursor._node._next is not self._header._next:
            yield cursor
            cursor = self._after(cursor)
        yield cursor


    @staticmethod
    def merge(lista1, lista2):
        #Supponiamo le liste ordinate senza effettuare esplicitamente un controllo

        if lista1.is_empty() and lista2.is_empty():
            raise ValueError("Le due liste sono vuote")


        if(lista1.last().element()<lista2.first().element()): # casi di liste consecutive
            return lista1 + lista2
        if(lista2.last().element()<lista1.first().element()): #
            return lista2 + lista1

        new_list = CircularPositionalList()
        cursor = lista1.first()
        cursor2 = lista2.first()



        i=j=0 # J è lungh di lista2 I è lungh di lista1

        while(i+j<(len(lista1)+len(lista2))):


            if( ( j==len(lista2) ) or ( (i< len(lista1)) and cursor.element()<cursor2.element() ) ):

                new_list.add_last(cursor.element())

                cursor = lista1._after(cursor)
                i+=1

            else:
                new_list.add_last(cursor2.element())

                cursor2 = lista2._after(cursor2)
                j+=1



        return new_list

    def bubblesorted(self):
        lungh = self._size - 1
        swap = True
        lista = self.copy()

        while(lungh > 0 and swap):
            swap = False
            pos = lista.first()
            for pos in lista._iter():

                if(pos.element() > lista._after(pos).element() and  pos != lista.last()):
                    swap = True
                    app = pos.element()
                    pos._node._element= pos._node._next._element
                    pos._node._next._element = app

            lungh-=1

        for elem in lista:
            yield elem



    # ------------------------------- magic methods -------------------------------
    def __add__(self, other):
        new_list = self.copy()
        for pos in other._iter():
            new_list.add_last(pos.element())
        return new_list

    def __contains__(self, p):
        try:
            node = self._validate(p)
        except Exception:
            return False

        return True

    def __len__(self):
        return self._size

    def __setitem__(self, p, value):
        self._validate(p)
        self.replace(p, value)

    def __getitem__(self, p):
        return self._validate(p)._element

    def __delitem__(self,p):
        self._validate(p)
        self.delete(p)

    def __iter__(self): # iteratore sugli elementi
        for pos in self._iter():
            yield pos.element()

    def __str__(self):
        lista = ""
        if(not self.is_empty()):
            lista = "Lista=["

            for pos in self._iter():
                if(pos != self.last()):

                    lista += str(pos.element())
                    lista += ","
                else :
                    lista += str(pos.element())

            lista += "]"

        else:
            print("LISTA VUOTA")

        return lista































































