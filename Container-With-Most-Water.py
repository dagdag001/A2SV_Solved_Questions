1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        l = 0
4        r = len(height) - 1
5        max_ = 0
6        while l < r:
7            w = r - l
8            if height[l] <= height[r]:
9                area = height[l] * w
10                l+=1
11                max_ = max(max_,area )
12            else:
13                area = height[r] * w
14                r-=1
15                max_ = max(max_,area )
16        return max_