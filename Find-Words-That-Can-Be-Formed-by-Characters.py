from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        def isSubset(word, characters):
            cc = Counter(characters)
            cw = Counter(word)
            for ch in cw:
                if cw[ch] > cc[ch]:
                    return False
            return True

        res = 0
        for word in words:
            if isSubset(word, chars):
                res += len(word)
        return res