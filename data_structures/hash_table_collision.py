class HashTable:
    def __init__(self):
        self.MAX = 10 #size of array
        self.arr = [[] for i in range(self.MAX)]
        self.dict = {}
        
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX
        
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for index, element in enumerate(self.arr[h]):
            print("index is: ", index)
            print("Element is :", element)
            if len(element) == 2 and element[0] == key:
                self.arr[h][index] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append((key, val))
        self.dict[key] = val
        
    def __getitem__(self, key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
        
    def __delitem__(self, key):
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]
        
t = HashTable()
print(t.get_hash("march 17"))
t["march 6"] = 29
t["January 23"] = 50
t["march 17"] = 80
print(t["march 17"])
print(t.dict)
print(t.arr)