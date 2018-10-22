from TdP_collections.list.positional_list import PositionalList

'''
La struttura dati implementata deriva da PositionalList (la quale deriva da DoubleLinkedList) e mostra le seguenti peculiarità:
- doppiamente concatenata: ogni nodo contiene un riferimento sia al nodo successivo (attraverso il campo next) che al precedente (campo prev).
L'implementazione ha previsto l'utilizzo di due sentinelle (o guardie): un nodo header e un nodo trailer, inseriti rispettivamente
all'inizio e alla fine della lista, e che non memorizzano elementi. L'utilizzo di questi nodi speciali è stato previsto per
semplificare la logica delle operazioni implementate (si pensi all'inserimento di un elemento nell'ultima posizione della lista).
Una lista vuota è inizializzata in maniera tale che il campo next del nodo header punti al trailer mentre il campo prev del nodo trailer
punti all'header. I succesivi inserimenti/rimozioni vengono effettuati tra una coppia di nodi esistenti.
- positional list: è stato aggiunto un ulteriore livello di astrazione attraverso l'ADT positional list utile a
nascondere i dettagli implementativi di un nodo e che meglio descrive la locazione di un nodo all'interno della lista
- circolare: il campo prev del primo elemento della lista contiene un riferimento all'ultimo nodo della lista
mentre il campo next dell'ultimo nodo contiene un riferimento al primo.
'''

class CircularPositionalList(PositionalList):

    # Restituisce:
    # - la Position precedente a "p", se un predecessore esiste
    # - None se "p" non ha un predecessore (la lista ha dimensione 1)
    # - ValueError se "p" non è una Position della lista
    def _before(self, p):
        if self._size == 1:
            return None
        else:
            return super().before(p)

    # Restituisce:
    # - la Position successiva a "p", se un successore esiste
    # - None se "p" non ha un successore (la lista ha dimensione 1)
    # - ValueError se "p" non è una Position della lista
    def _after(self, p):
        if self._size == 1:
            return None
        else:
            return super().after(p)

    # Restituisce l'elemento contenuto nella Position precedente a "p" sfruttando il metodo privato _before
    def before(self, p):
        if self._size == 1:
            return None
        return self._before(p).element()

    # Restituisce l'elemento contenuto nella Position successiva a "p" sfruttando il metodo privato _after
    def after(self, p):
        if self._size == 1:
            return None
        return self._after(p).element()

    # Restituisce True se la lista è vuota, False altrimenti
    def Is_empty(self):
        return super().is_empty()

    # Restituisce True se la lista è ordinata, False altrimenti
    def Is_sorted(self):
        for pos in self._iter():
            if self._validate(pos)._element > self._validate(pos)._next._element and self._validate(pos)._next != self._header._next:
                return False
        return True

    # Aggiunge l'elemento "e" in cima alla lista e restituisce la Position corrispondente
    def add_first(self, e):
        node = self._header._next

        if self.is_empty():
            new_node = self._Node(e, None, None)
            new_node._prev = new_node
            new_node._next = new_node

            self._trailer._prev = new_node
            self._header._next = new_node
            self._size += 1
            return self._make_position(new_node)
        else:
            new_pos = self._insert_between(e, self._trailer._prev, node)  # Inserisce "e" tra l'ultimo nodo della lista (predecessore) e il primo (successore)
            self._header._next = new_pos._node  # L'header deve puntare al nodo contenente "e"

            return new_pos

    # Aggiunge l'elemento "e" in coda alla lista e restituisce la Position corrispondente
    def add_last(self, e):
        node = self._trailer._prev

        if self.is_empty():
            new_node = self._Node(e, None, None)
            new_node._prev = new_node
            new_node._next = new_node

            self._trailer._prev = new_node
            self._header._next = new_node
            self._size += 1
            return self._make_position(new_node)
        else:
            new_pos = self._insert_between(e, node, self._header._next)  # Inserisce "e" tra l'ultimo nodo della lista (predecessore) e il primo (successore)
            self._trailer._prev = new_pos._node  # Il trailer deve puntare al nodo contenente "e"
            return new_pos

    # Aggiunge l'elemento "e" alla lista prima della Position "p" e restituisce la Position corrispondente
    def add_before(self, p, e):
        node = self._validate(p)

        if node._prev == self._trailer._prev:  # Caso in cui la Position "p" è in prima posizione... urge mantenere la circolarità
            return self.add_first(e)
        else:
            return super().add_before(p, e)

    # Aggiunge l'elemento "e" alla lista prima della Position "p" e restituisce la Position corrispondente
    def add_after(self, p, e):
        node = self._validate(p)

        if node._next == self._header._next:  # Caso in cui la Position "p" è in ultima posizione... urge mantenere la circolarità
            return self.add_last(e)
        else:
            return super().add_after(p, e)

    # Restituisce la Position corrispondente alla prima occorrenza dell'elemento "e", None se non presente
    def find(self, e):
        if e is None:
            raise ValueError("E non è un elemento")
        for pos in self._iter():
            if pos._node._element == e:
                return pos
        return None

    # Rimuove la Position "p" dalla lista, la invalida e restituisce l'elemento contenuto
    def delete(self, p):
        original = self._validate(p)

        if p == self.first():  # Cancellazione della Position in cima alla lista
            self._header._next = p._node._next  # L'header deve puntare al nodo successivo
            self.last()._node._next = p._node._next  # L'ultimo elemento della lista deve puntare all'elemento successivo al primo
        elif p == self.last():  # Cancellazione della Position in coda alla lista
            self._trailer._prev = p._node._prev  # Il trailer deve puntare al nodo che precede l'ultimo
            p._node._prev._next = p._node._next  # Il nodo che precede l'ultimo deve puntare al next di quello da rimuovere (al primo della lista)
        return self._delete_node(original)  # inherited method returns element

    # Rimuove tutti gli elementi dalla lista, invalidando le relative Position
    def clear(self):
        cursor = self.first()

        while cursor._node._next is not cursor._node:  # Non posso usare header->_next poichè ad ogni passo cancello un elemento
            next_node = cursor._node._next
            self.delete(cursor)
            cursor = self._make_position(next_node)
        self.delete(self.last())

    # Restituisce il numero di occorrenze di "e" nella lista
    def count(self, e):
        cont = 0
        for pos in self._iter():
            if pos._node._element == e:
                cont += 1
        return cont

    # Ribalta la lista (metodo in-place)
    def reverse(self):
        lista_appoggio = []

        for pos in self._iter():
            lista_appoggio.append(pos._node._element)
        for pos in self._iter():
            pos._node._element = lista_appoggio.pop()

    # Restituisce una nuova lista con gli stessi elementi e lo stesso ordine
    def copy(self):
        new_list = CircularPositionalList()

        for pos in self._iter():
            new_list.add_last(pos._node._element)
        return new_list

    # Restituisce un generatore sulle Position della lista
    def _iter(self):
        cursor = self.first()
        while cursor._node._next is not self._header._next:
            yield cursor
            cursor = self._after(cursor)
        yield cursor

    # Restituisce un generatore tramite cui è possibile ottenere gli elementi della lista in ordine (senza modificare l'ordinamento della lista)
    def bubblesorted(self):
        lungh = self._size - 1
        swap = True
        lista = self.copy()

        while lungh > 0 and swap:
            swap = False
            pos = lista.first()
            for pos in lista._iter():

                if pos.element() > lista._after(pos).element() and pos != lista.last():
                    swap = True
                    app = pos.element()
                    pos._node._element = pos._node._next._element
                    pos._node._next._element = app
            lungh -= 1
        for elem in lista:
            yield elem

    # Restituisce una nuova lista ordinata nata dalla fusione tra "lista1" e "lista2" (supposte ordinate)
    @staticmethod
    def merge(lista1, lista2):
        if lista1.is_empty() and lista2.is_empty():
            raise ValueError("Le due liste sono vuote")

        # Essendo le due liste ordinate, se l'ultimo elemento di una delle due liste è < del primo elemento dell'altra, è sufficiente concatenarle
        if lista1.last().element() < lista2.first().element():  # casi di liste consecutive
            return lista1 + lista2
        if lista2.last().element() < lista1.first().element():
            return lista2 + lista1

        new_list = CircularPositionalList()
        cursor1 = lista1.first()
        cursor2 = lista2.first()

        i = j = 0  # "j" è lunghezza di lista2 mentre "i" quella di lista1

        while i + j < (len(lista1) + len(lista2)):
            if (j == len(lista2)) or (i < len(lista1) and cursor1.element() < cursor2.element()):
                new_list.add_last(cursor1.element())
                cursor1 = lista1._after(cursor1)
                i += 1
            else:
                new_list.add_last(cursor2.element())
                cursor2 = lista2._after(cursor2)
                j += 1
        return new_list

    # ------------------------------- magic methods -------------------------------
    # x + y
    def __add__(self, other):
        new_list = self.copy()
        for pos in other._iter():
            new_list.add_last(pos.element())
        return new_list

    # p in x
    def __contains__(self, p):
        try:
            node = self._validate(p)
        except Exception:
            return False
        return True

    # len(x)
    def __len__(self):
        return self._size

    # x[p] = e
    def __setitem__(self, p, value):
        self._validate(p)
        self.replace(p, value)

    # x[p]
    def __getitem__(self, p):
        return self._validate(p)._element

    # del x[p]
    def __delitem__(self, p):
        self._validate(p)
        self.delete(p)

    def __iter__(self):  # Iteratore sugli elementi
        for pos in self._iter():
            yield pos.element()

    def __str__(self):
        lista = ""
        if not self.is_empty():
            lista = "Lista=["

            for pos in self._iter():
                if pos != self.last():

                    lista += str(pos.element())
                    lista += ","
                else:
                    lista += str(pos.element())
            lista += "]"
        else:
            print("LISTA VUOTA")
        return lista
