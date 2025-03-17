class _Node:
    """LightWeight, nonpublic class for storing a singly linked node"""
    __slot__ = ('_element', '_next', '_prev')
    
    def __init__(self, element, next = None, prev = None):
        self._element = element
        self._next = next
        self._prev = prev
