from LinkedQueue import _LinkedQueue
from QuickSort import quick_sort

lq = _LinkedQueue()

lq.enqueue(50)
lq.enqueue(30)
lq.enqueue(80)
lq.enqueue(70)
lq.enqueue(40)
lq.enqueue(10)

print("정렬 전 리스트 :")
for i in range(len(lq)):
    print(lq.dequeue())
    
lq.enqueue(50)
lq.enqueue(30)
lq.enqueue(80)
lq.enqueue(70)
lq.enqueue(40)
lq.enqueue(10)
    
quick_sort(lq)

print("정렬 후 리스트 :")
for i in range(len(lq)):
    print(lq.dequeue())