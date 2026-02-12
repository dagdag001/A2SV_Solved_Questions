1class Solution:
2    def findValidPair(self, s: str) -> str:        
3        freq = Counter(s)      
4        n = len(s)
5        for i in range(n - 1):
6            a = s[i]
7            b = s[i + 1]
8            if a != b:
9                if freq[a] == int(a) and freq[b] == int(b):
10                    return a + b
11        
12        return ""
13