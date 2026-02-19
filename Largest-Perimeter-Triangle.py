1class Solution:
2    def largestPerimeter(self, nums: List[int]) -> int:
3        x = sorted(nums)[::-1]
4        for i in range(len(x) - 2):
5            if x[i+1] + x[i+2] > x[i]:
6                return sum(x[i:i+3])
7        return 0
8