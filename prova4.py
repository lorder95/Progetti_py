from CircularPositionalList import CircularPositionalList

lista = CircularPositionalList()
lista2 = CircularPositionalList()
p4 = lista2.add_first(2)

p1 = lista.add_last(8)
p2 = lista.add_last(15)
p3 = lista.add_first(55)
del lista[p3]
#lista.add_first(88)
#lista.add_before(lista.add_first(12), 88)

#for pos in lista._iter():
#    print(pos.element())

for elem in lista:
        print(elem)

print(lista.Is_sorted())
print(lista[p2])
lista[p2] = 26
print(lista[p2])
print(p4 in lista)
#print(lista.find(None).element())

print(lista.count(26))

lista3 = CircularPositionalList.merge(lista, lista2)
print(lista3)