from CircularPositionalList import CircularPositionalList


class InteractiveCircular():

        def __init__(self):
            self._list = CircularPositionalList()

            while True:
                print("**********************************")
                print("******CircularPositionalList (len = {0})".format(len(self._list)))

                print("1) Stampa tutti gli elementi")
                print("2) Restituisci elemento in cima")
                print("3) Restituisci elemento in coda")
                print("4) Verifica se la lista è ordinata")
                print("5) Aggiunti elemento in cima")
                print("6) Aggiungi elemento in coda")
                print("7) Verifica se la lista contiene un elemento")
                print("8) Rimuovi tutti gli elementi")
                print("9) Inverti ordine elementi")
                print("10) Stampa tutti gli elementi in ordine")
                print("0) Esci")

                try:
                    choice = int(input("Inserisci un numero: "))

                    if choice == 1:
                        self._print_all()
                    elif choice == 2:
                        self._get_first()
                    elif choice == 3:
                        self._get_last()
                    elif choice == 4:
                        self._is_sorted()
                    elif choice == 5:
                        self._add_first()
                    elif choice == 6:
                        self._add_last()
                    elif choice == 7:
                        self._contains()
                    elif choice == 8:
                        self._clear()
                    elif choice == 9:
                        self._reverse()
                    elif choice == 10:
                        self._bubble_sort()
                    elif choice == 0:
                        exit(0)
                    else:
                        print("!! Operazione non implementata !!")
                except ValueError:
                    print("!! Parametro non corretto !!")

                input("(Premi un tasto per tornare al menù principale)\n")

        def _get_first(self):
            print(self._list.first().element())

        def _get_last(self):
            print(self._list.last().element())

        def _is_sorted(self):
            if self._list.is_empty():
                print("!! La lista è vuota !!")
                return

            if self._list.Is_sorted():
                print("->La lista è ordinata")
            else:
                print("->La lista NON è ordinata")

        def _add_first(self):
            e = input("Inserisci un elemento: ")
            self._list.add_first(int(e))

        def _add_last(self):
            e = input("Inserisci un elemento: ")
            self._list.add_last(int(e))

        def _contains(self):
            e = input("Inserisci un intero: ")
            if e in self._list:
                print("->Elemento presente")
            else:
                print("->Elemento non presente")

        def _clear(self):
            self._list.clear()

        def _reverse(self):
            if self._list.is_empty():
                print("!! La lista è vuota !!")
                return

            self._list.reverse()

        def _bubble_sort(self):
            if self._list.is_empty():
                print("!! La lista è vuota !!")
                return

            sorted_list = self._list.bubblesorted()

            for e in sorted_list:
                print("-->" + str(e))

        def _print_all(self):
            if self._list.is_empty():
                print("!! La lista è vuota !!")
                return

            for e in self._list:
                print("-->" + str(e))

InteractiveCircular()