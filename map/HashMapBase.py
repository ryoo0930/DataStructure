import MapBase
import random
class HashMapBase(MapBase):
    def __init__(self, cap = 11, p = 109345121):
        self._table = cap * [None]
        self._n = 0
        self._prime = p
        self._scale = 1 + random.randrange(p - 1)
        self._shift = random.randrange(p)
        
    def _hash_function(self, k):
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)
    
    def __len__(self):
        return self._n
    
    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k) # 이거 잘 모르겠음. _bucket_getitem 함수가 어디서 나온거지?
    
    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table) - 1)
            
    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -= 1
        
    def _resize(self, c):
        old = list(self.items())
        self._table = c * [None]
        self._n = 0
        for (k, v) in old:
            self[k] = v