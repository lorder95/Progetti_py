from CircularPositionalList import CircularPositionalList


lista = CircularPositionalList()

pos1=lista.add_first(1) # TESTO METODI ADD FIRST E ADDLAST E Conservo le position di primo e ultimo per effettuare dei test successivamente
lista.add_last(2)
lista.add_last(3)
lista.add_last(4)
pos5=lista.add_last(5)
print("LISTA INIZIALE")
print(lista)
print("\n")

print("*****TEST METODI:")
print("FIRST:"+str(lista.first().element())+" LAST: "+ str(lista.last().element()))
print("BEFORE DEL PRIMO:"+str(lista.before(pos1))+" AFTER DELL'ULTIMO:"+str(lista.after(pos5))) # IN QUESTO MODO TESTIAMO ANCHE LA CIRCOLARITA'
print("Count(3)= "+str(lista.count(3)))
print("IS SORTED= "+str(lista.Is_sorted()) +" IS EMPTY="+ str(lista.is_empty()))

print("ADD_AFTER:(aggiungo 6 dopo 5) = " +str(lista.add_after(pos5,6).element()))
print("ADD_BEFORE:(aggiungo 0 prima di 1) = " +str(lista.add_before(pos1,0).element()))


print("\nLISTA DOPO AGGIUNTE: ")
print(lista)
print("Verifico che la circolarità sia preservata:")
print("BEFORE DEL PRIMO:"+str(lista.before(lista.first()))+" AFTER DELL'ULTIMO:"+str(lista.after(lista.last()))) # VERIFICO CHE MANTIENE CORRETTAMENTE LA CIRCOLARITA'

print("Find(6) = "+str(lista.find(6).element()))

print("Replace 6 con 7 = "+str(lista.replace(lista.last(),7))+" <-- VECCHIO ELEMENTO")
print("\nLista Nuova")
print(lista)

print("Elimino 7 e Stampa Lista dopo eliminazione")
lista.delete(lista.last())
print(lista)


print("\nVerifico che la circolarità sia preservata:")
print("BEFORE DEL PRIMO:"+str(lista.before(lista.first()))+" AFTER DELL'ULTIMO:"+str(lista.after(lista.last()))) # VERIFICO CHE MANTIENE CORRETTAMENTE LA CIRCOLARITA'

print("\nCreo altre due liste con metodo copy() { LISTA2 e LISTA3 }")

lista2 = lista.copy()
lista3 = lista.copy()

print("ED ESEGUO LA REVERSE SU LISTA ")
lista.reverse()
print(lista)

print("ED ESEGUO LA REVERSE SU LISTA2 ")
lista2.reverse()
print(lista2)

print("ED ESEGUO LA REVERSE SU LISTA3 ")
lista3.reverse()
print(lista3)

print("CLEAR SU LISTA3")
lista3.clear()
print("Prova di stampa di lista3 dopo clear:\n")
print("Lista3:")
print(str(lista3))

print("***TEST OPERATORI ")
print("LISTA1 + LISTA2 --> "+str(lista+lista2))
print("CONTAINS di 1 in LISTA1= "+str(pos1 in lista)+" ; E OPERATORE X[p] con position di 1 = "+ str(lista[pos1]))
print("LUNGHEZZA LISTA 1 = "+str(len(lista)))

lista[pos5]=7
print("ASSEGNAMENTO X[p]=e  (lista[pos5]=7)  sostituisco 5 con 7 ")
print(lista)

del lista[lista.last()]
print("ELIMINO 7 e stampo lista (Operatore del x[p] ):")
print(lista)

print("\nStampa lista con iteratore:")
for elem in lista:
    print(elem)

print("***TEST MERGE")
print("Lista1 ->"+str(lista))
print("Lista2 ->"+str(lista2))
print("LisaMerged  "+str(CircularPositionalList.merge(lista,lista2)))


print("*** TEST GENERATORE BUBBLESORTED")
print("Modifico la lista 1 rendendola disordinata:")
lista.add_first(10)
lista.add_first(22)
print("Lista disordinata --> "+str(lista))

print("UTILIZZO GENERATORE:")
for elem in lista.bubblesorted():
    print(elem)
