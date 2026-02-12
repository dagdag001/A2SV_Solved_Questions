1class Solution:
2    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
3        cr = Counter(ransomNote)
4        cm = Counter(magazine)
5        for i in cr:
6            if cr[i] > cm[i]:
7                return False
8        return True
9        