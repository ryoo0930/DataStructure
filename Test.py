from PositionalList import _PositionalList

pl = _PositionalList()
pl.add_first(10)
pl.add_first(20)
pl.add_last(40)

print(list(pl))

pos = pl.first()
pl.add_after(pos, 30)

print(list(pl))

pos = pl.after(pl.first())
pl.add_before(pos, 90)

print(list(pl))

pl.add_after(pos, 70)

print(list(pl))