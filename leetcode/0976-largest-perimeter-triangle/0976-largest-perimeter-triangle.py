class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        x = sorted(nums)[::-1]
        for i in range(len(x) - 2):
            if x[i+1] + x[i+2] > x[i]:
                return sum(x[i:i+3])
        return 0
