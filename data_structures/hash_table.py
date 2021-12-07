class HashTable:
    def __init__(self):
        self.MAX = 100 #size of array
        self.arr = [None for i in range(self.MAX)]
        self.dict = {}
        
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
        
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val
        self.dict[key] = val
        
    def __getitem__(self, key):
        h = self.get_hash(key)
        print(self.dict)
        return self.arr[h]
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
        
t = HashTable()
print(t.get_hash("march 17"))
t["march 6"] = 29
t["January 23"] = 50
t["march 17"] = 80
print(t["march 17"])
print(t.dict)