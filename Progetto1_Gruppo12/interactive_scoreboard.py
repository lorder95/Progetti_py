from datetime import datetime

from scoreboard import ScoreBoard


class InteractiveConsole():

    def __init__(self):
        print("Creazione ScoreBoard in corso...")

        try:
            capacity = int(input("Inserisci la capacità (default = 10): "))
        except ValueError:
            capacity = 10
            print("!! Usato il parametro di default !!")
        self._scoreboard = ScoreBoard(capacity)

        while True:
            print("**********************************")
            print("******ScoreBoard (dim = {0})".format(capacity))
            if self._scoreboard.Is_empty():
                print("******Attualmente vuoto")
            elif self._scoreboard.size() == capacity:
                print("******Attualmente pieno")
            else:
                print("******Contiene {0} score".format(self._scoreboard.size()))
            print("1) Inserisci uno score")
            print("2) Visualizza i migliori risultati")
            print("3) Visualizza i peggiori risultati")
            print("0) Esci")

            try:
                choice = int(input("Inserisci un numero: "))

                if choice == 1:
                    self._inserisci_score()
                elif choice == 2:
                    self._stampa_score(0)
                elif choice == 3:
                    self._stampa_score(1)
                elif choice == 0:
                    exit(0)
                else:
                    print("!! Operazione non implementata !!")
            except ValueError:
                print("!! Parametro non corretto !!")

            input("(Premi un tasto per tornare al menù principale)")

    def _inserisci_score(self):
        player_name = input("Inserisci il nome del giocatore: ")

        try:
            player_score = float(input("Inserisci lo score: "))
        except ValueError:
            print("!! Immesso uno score non valido !!")
            return

        try:
            player_date = input("Inserisci una data nel formato GG/MM/YYYY: ")
            datetime.strptime(player_date, "%d/%m/%Y")
        except ValueError:
            print("!! Immessa data nel formato scorretto !!")
            player_date = "{:%d/%m/%Y}".format(datetime.now())
            print("!! Uso data odierna ({0}) !!".format(player_date))

        try:
            score = ScoreBoard._Score(player_name, player_score, player_date)
            self._scoreboard.insert(score)
            print("->Score aggiunto")
        except Exception as e:
            print("!! " + str(e) + " !!")
        except:
            print(" !! Lo score è già stato inserito !! ")

    def _stampa_score(self, mode):
        if self._scoreboard.size() == 0:
            print("->Lo ScoreBoard è vuoto...")
        else:
            try:
                n_score = int(input("Inserisci il numero di score che vuoi stampare (default = 1): "))
            except ValueError:
                n_score = 1
                print("!! Usato il parametro di default !!")

            if mode == 0:
                lista = self._scoreboard.top(n_score)
            elif mode == 1:
                lista = self._scoreboard.last(n_score)

            '''
            for i, pos in enumerate(lista):
                print("******* SCORE {0} *******".format(i+1))
                print("Player name: " + pos.element()._namePlayer)
                print("Score: " + str(pos.element()._scorePlayer))
                print("Date: " + pos.element()._data)
            '''

InteractiveConsole()
