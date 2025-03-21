from DoublyLinkedBase import _DoublyLinkedBase

class _LinkedDeque(_DoublyLinkedBase):
    
    def first(self):
        if self.is_empty():
            raise print("Deque is empty")
        return self._header._next._element
    
    def last(self):
        if self.is_empty():
            raise print("Deque is empty")
        return self._trailer._prev._element
    
    def insert_first(self, e):
        self._insert_between(e, self._header, self._header._next)
    
    def insert_last(self, e):
        self._insert_between(e, self._trailer._prev, self._trailer)
        
    def delete_first(self):
        if self.is_empty():
            raise print("Deque is empty")
        return self._delete_node(self._header._next)
    
    def delete_last(self):
        if self.is_empty():
            raise print("Deque is empty")
        return self._delete_node(self._trailer._prev)
    
    def __iter__(self):
        current = self._header._next
        while current is not self._trailer:
            yield current._element
            current = current._next
            
