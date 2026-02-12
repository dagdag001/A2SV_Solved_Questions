1class Solution:
2    def frequencySort(self, s: str) -> str:
3        freq = Counter(s)
4        res = sorted(s, key=lambda n: (-freq[n], n))
5        return "".join(res)