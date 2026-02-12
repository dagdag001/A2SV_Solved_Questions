class Solution:
    def findValidPair(self, s: str) -> str:        
        freq = Counter(s)      
        n = len(s)
        for i in range(n - 1):
            a = s[i]
            b = s[i + 1]
            if a != b:
                if freq[a] == int(a) and freq[b] == int(b):
                    return a + b
        
        return ""
