from TdP_collections.list.positional_list import PositionalList
from CircularPositionalList import CircularPositionalList

list = CircularPositionalList()



print(list.before(list.add_last(1)))

print(list.before(list.add_last(2))._node._element)
list.add_last(3)
list.add_last(4)

list2 = CircularPositionalList()
list2.add_last(5)
list2.add_last(6)
list2.add_last(7)
list2.add_last(8)


lista3 = list + list2

print(lista3)


p = lista3.after(lista3.add_first(100))
print(p)
#lista3.delete(p)

lista3.__delitem__(p)
print(lista3)

print(lista3[lista3.add_first(200)]) # Test del get item


pos300 = lista3.add_first(300)

print(lista3)

print(pos300 in lista3)
