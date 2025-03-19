class _LinkedQueue:
    
    class _Node:
        
        __slot__ = ('_element', 'next')
        
        def __init__(self, element, next):
            self._element = element
            self._next = next
            
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise print("Queue is empty")
        return self._head._element
    
    def dequeue(self):
        if self.is_empty():
            raise print("Queue is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer
    
    def enqueue(self, e):
        newNode = self._Node(e, None)
        if self.is_empty():
            self._head = newNode
        else:
            self._tail._next = newNode
        self._tail = newNode
        self._size += 1
        
        