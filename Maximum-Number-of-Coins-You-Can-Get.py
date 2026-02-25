1class Solution:
2    def maxCoins(self, piles: List[int]) -> int:
3        x = sorted(piles)[::-1]
4        res = 0
5        idx = 1
6        if not piles:
7            return 0
8        for i in range(len(x) // 3):
9            res+=x[idx]
10            idx+=2
11        return res
12