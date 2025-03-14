from MyList import MyList

class ArrayBasedList(MyList):
    """List implemented by Array"""
    length = 0
    
    def __init__(self, size):
        self.item = size * [None]
        self.length = 0
        
    def len(self):
        return self.length
    
    def getitem(self, j):
        if(self.length > j):
            return self.item[j]
        raise ValueError("Value not in list")
    
    def setitem(self, val, j):
        if(self.length > 1):
            self.item[j] = val
            return
        raise ValueError("Index is out of bound")