1class FrequencyTracker:
2
3    def __init__(self):
4        self.count = defaultdict(int)      
5        self.freq = defaultdict(int)      
6
7    def add(self, number: int) -> None:
8        old = self.count[number]
9        
10        if old > 0:
11            self.freq[old] -= 1
12        
13        self.count[number] += 1
14        new = self.count[number]
15        self.freq[new] += 1
16
17    def deleteOne(self, number: int) -> None:
18        old = self.count[number]
19        
20        if old == 0:
21            return
22        
23        self.freq[old] -= 1
24        self.count[number] -= 1
25        
26        new = self.count[number]
27        if new > 0:
28            self.freq[new] += 1
29
30    def hasFrequency(self, frequency: int) -> bool:
31        return self.freq[frequency] > 0