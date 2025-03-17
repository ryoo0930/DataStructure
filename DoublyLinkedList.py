from DoublyLinkedBase import _DoublyLinkedBase

class DoubleLinkedList(_DoublyLinkedBase):
    def insert_first(self, element):
        return self._insert_between(element, self.header, self.header._next)
    
    def insert_last(self, element):
        return self._insert_between(element, self.tailer._prev, self.tailer)
    
    def delete_first(self):
        if self.is_empty():
            raise Exception("List is empty")
        return self._delete_node(self.header._next)
    
    def delete_last(self):
        if self.is_empty():
            raise Exception("List is empty")
        return self._delete_node(self.tailer._prev)
    
    def __iter__(self):
        current = self.header._next
        while current is not self.tailer:
            yield current._element
            current = current._next
            
dll = DoubleLinkedList()
dll.insert_first(10)
dll.insert_last(5)
dll.insert_last(15)

print("현재 리스트 : ", list(dll))

dll.delete_first()
print("첫번째 원소 삭제 이후 : ", list(dll))

dll.delete_last()
print("마지막 원소 삭제 이후 : ", list(dll))