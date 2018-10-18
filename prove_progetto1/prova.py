from TdP_collections.list.positional_list import PositionalList
from CircularPositionalList import CircularPositionalList

lista = CircularPositionalList()

lista.add_last(1)
lista.add_last(2)
lista.add_last(3)
pos4= lista.add_last(4)
lista.add_last(5)

print("LISTA INIZIALE")
#for elem in lista:
   # print(elem._node._element)
print(lista)

print("LISTA CON ALCUNI ELEM AGGIUNTI")
lista.add_first(10)
lista.add_first(9)
lista.add_first(10)
lista.add_last(10)


#for elem in lista:
   # print(elem._node._element)
print(lista)

print("Occorrenze elemento 10 ="+str(lista.count(10)))


lista.reverse()
print("LISTA DOPOO REVERSE")
#for elem in lista:
 #   print(elem._node._element)
print(lista)

print("LISTA IS_SORTED:"+str(lista.Is_sorted()))

print("FIND DI 4: "+str(lista.find(4).element())) # Lista.find(4) restituisce la position per cui applico metodo element() per visualizzarne il valore


print("TEST BEFORE: BEFORE di BEFORE di 10 è  = " +str(lista.before(lista.before(lista.find(10))).element())) # Così si dimostra anche la circolarità della lista

print("TEST AFTER: AFTER di AFTER di 9 è  = " +str(lista.after(lista.after(lista.find(9))).element())) # Così si dimostra anche la circolarità della lista


print("LISTA COPIATA:")

lista2 = lista.copy()

#for elem in lista2:
 #   print(elem.element())
print(lista2)



lista.clear()
print("CANCELLATA")



print("DIMENSIONE LISTA 1: "+str(lista._size))
print("DIMENSIONE LISTA 2: "+str(lista2._size))

#SE SI PROVA A STAMPARE ORA CHE SONO STATI ELIMINATI GLI ELEMENTI DA ERRORE POICHE' VUOTA
#for elem in lista:
 #   print(elem._node._element)

print(lista)




