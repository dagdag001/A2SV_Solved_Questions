class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        x = sorted(piles)[::-1]
        res = 0
        idx = 1
        if not piles:
            return 0
        for i in range(len(x) // 3):
            res+=x[idx]
            idx+=2
        return res
