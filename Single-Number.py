1class Solution:
2    def singleNumber(self, nums: List[int]) -> int:
3        cn = Counter(nums)
4        for i in cn:
5            if cn[i] == 1:
6                return i