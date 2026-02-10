1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        longest = 0
4        set_nums = set(nums) 
5        for  num in set_nums:
6            if num-1 not in set_nums:
7                count = 1
8                j = 1 
9                while num + j in set_nums:
10                    count+=1
11                    j +=1
12                longest = max(longest , count) 
13        return longest