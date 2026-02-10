class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        set_nums = set(nums) 
        for  num in set_nums:
            if num-1 not in set_nums:
                count = 1
                j = 1 
                while num + j in set_nums:
                    count+=1
                    j +=1
                longest = max(longest , count) 
        return longest