from _Node import _Node

class _DoublyLinkedBase(_Node):
    
    def __init__(self):
        self.header = self._Node(None, None, None)
        self.tailer = self._Node(None, None, None)
        self._header._next = self.tailer
        self._tailer._prev = self.header
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def _insert_between(self, element, PrevNode, NextNode):
        newNode = self._Node(element, PrevNode, NextNode)
        PrevNode._next = newNode
        NextNode._prev = newNode
        self._size += 1
        return newNode
    
    def _delete_node(self, node):
        PrevNode = node._prev
        NextNode = node._next
        PrevNode._next = NextNode
        NextNode._prev = PrevNode
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element