from LinkedDeque import _LinkedDeque

ld = _LinkedDeque()
ld.insert_first(20)
ld.insert_first(30)
ld.insert_last(50)
ld.insert_last(60)

print(list(ld))