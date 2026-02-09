class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for index, value in enumerate(nums):
            h[value] = index
        for i in range(len(nums)):
           complement = target - nums[i]
           if complement in h and i != h[complement]:
                return [i, h[complement]]
   
