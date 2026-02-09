1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        h = {}
4        for index, value in enumerate(nums):
5            h[value] = index
6        for i in range(len(nums)):
7            complement = target - nums[i]
8            if complement in h and i != h[complement]:
9                return [i, h[complement]]
10        
11