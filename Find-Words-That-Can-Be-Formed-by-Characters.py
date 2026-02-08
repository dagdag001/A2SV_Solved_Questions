1class Solution:
2    def countCharacters(self, words: List[str], chars: str) -> int:
3        def isSubset(word, characters):
4            cc = Counter(characters)
5            cw = Counter(word)
6            for ch in cw:
7                if cw[ch] > cc[ch]:
8                    return False
9            return True
10
11        res = 0
12        for word in words:
13            if isSubset(word, chars):
14                res+=len(word)
15        return res