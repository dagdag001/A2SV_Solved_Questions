class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        res = sorted(s, key=lambda n: (-freq[n], n))
        return "".join(res)