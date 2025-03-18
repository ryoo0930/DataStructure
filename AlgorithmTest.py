from PositionalList import _PositionalList
from BinarySearch import binary_search

pl = _PositionalList()
for i in range(5):
    value = 100 - (i * 10)
    pl.add_first(value)
    
    
print(list(pl))
data = list(pl)

target = 70
print("target :", target, "\'s index :", binary_search(data, target, 0, len(data) - 1))