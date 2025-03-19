from LinkedQueue import _LinkedQueue

lq = _LinkedQueue()

for i in range(5):
    value = 100 - (i * 10)
    lq.enqueue(value)
    
for i in range(5):
    print(lq.dequeue())