1class Solution:
2    def closeStrings(self, word1: str, word2: str) -> bool:
3        if len(word1) != len(word2):
4            return False
5        
6        c1 = Counter(word1)
7        c2 = Counter(word2)
8        
9        if set(c1.keys()) != set(c2.keys()):
10            return False        
11        if sorted(c1.values()) != sorted(c2.values()):
12            return False
13        
14        return True