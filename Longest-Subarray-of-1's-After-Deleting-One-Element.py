1class Solution:
2    def longestSubarray(self, nums: List[int]) -> int:
3        max_ = 0
4        l = 0
5        r = 0
6        zero_count = 0
7        for r in range(len(nums)):
8            if nums[r] == 0:
9                zero_count +=1
10            while zero_count > 1:
11                if nums[l] == 0:
12                    zero_count -=1
13                l+=1
14            max_ = max(max_, r - l)
15        return max_
16
17
18