class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cr = Counter(ransomNote)
        cm = Counter(magazine)
        for i in cr:
            if cr[i] > cm[i]:
                return False
        return True
        