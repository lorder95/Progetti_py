from TdP_collections.list.positional_list import PositionalList
from Progetti.Progetto1_Gruppo12.CircularPositionalList import CircularPositionalList
lista = CircularPositionalList()
lista2 = CircularPositionalList()

lista.add_last(0)
lista.add_last(2)
lista.add_last(10)

lista2.add_last(3)
lista2.add_last(4)

print(CircularPositionalList.merge(lista,lista2))
