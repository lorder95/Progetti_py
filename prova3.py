from TdP_collections.list.positional_list import PositionalList
from Progetti.CircularPositionalList import CircularPositionalList

list = CircularPositionalList()

pos1= list.add_last(1)
pos2=list.add_last(1)
pos3=list.add_last(7)
pos4= list.add_last(13)
pos4= list.add_last(14)

list2 = CircularPositionalList()

list2.add_last(2)
list2.add_last(2)
list2.add_last(6)
list2.add_last(20)

lista3 = list.merge(list2)

print(lista3)

lista4 = CircularPositionalList()
lista4.add_last(5)
lista4.add_last(3)
lista4.add_last(6)
lista4.add_last(1)

lista_ordinata = lista4.bubblesorted()
#print(lista_ordinata.next())

print("GENERATORE---> "+str(lista_ordinata))
for elem in lista_ordinata:
    print(elem)


print(lista4)


# prova github
