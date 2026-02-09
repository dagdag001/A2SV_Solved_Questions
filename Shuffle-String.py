1class Solution:
2    def restoreString(self, s: str, indices: List[int]) -> str:
3        n = len(s)
4        h = {}
5        j = 0
6        h = list(zip(s, indices))
7        print(h)
8        print(n)
9        res = [""] * n
10        for i in h:
11            res[i[1]] = i[0]
12        return "".join(res)