class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_ = 0
        l = 0
        r = 0
        zero_count = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zero_count +=1
            while zero_count > 1:
                if nums[l] == 0:
                    zero_count -=1
                l+=1
            max_ = max(max_, r - l)
        return max_


