1class Solution:
2    def minimumIndex(self, nums: List[int]) -> int:
3        n = len(nums)        
4        candidate = None
5        count = 0
6        for num in nums:
7            if count == 0:
8                candidate = num
9            count += 1 if num == candidate else -1
10        
11        total = nums.count(candidate)
12        
13        left_count = 0
14        
15        for i in range(n - 1):
16            if nums[i] == candidate:
17                left_count += 1
18            
19            left_len = i + 1
20            right_len = n - left_len
21            right_count = total - left_count
22            
23            if left_count > left_len // 2 and right_count > right_len // 2:
24                return i
25        
26        return -1