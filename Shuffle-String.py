class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        h = {}
        j = 0
        h = list(zip(s, indices))
        print(h)
        print(n)
        res = [""] * n
        for i in h:
            res[i[1]] = i[0]
        return "".join(res)