1class RandomizedSet:
2
3    def __init__(self):
4        self.arr = []
5        self.pos = {}
6        
7
8    def insert(self, val: int) -> bool:
9        if val in self.pos:
10            return False
11        self.arr.append(val)
12        self.pos[val] = len(self.arr) - 1 #last index
13        return True
14
15    def remove(self, val: int) -> bool:
16        if val not in self.pos:
17            return False
18        idx = self.pos[val]              
19        last = self.arr[-1]              
20
21        self.arr[idx] = last
22        self.pos[last] = idx
23
24        self.arr.pop()
25        del self.pos[val]
26
27        return True
28        
29
30    def getRandom(self) -> int:
31        idx = random.randint(0, len(self.arr) - 1)
32        return self.arr[idx]
33
34        
35        
36
37
38# Your RandomizedSet object will be instantiated and called as such:
39# obj = RandomizedSet()
40# param_1 = obj.insert(val)
41# param_2 = obj.remove(val)
42# param_3 = obj.getRandom()