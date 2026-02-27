class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_ = 0
        while l < r:
            w = r - l
            if height[l] <= height[r]:
                area = height[l] * w
                l+=1
                max_ = max(max_,area )
            else:
                area = height[r] * w
                r-=1
                max_ = max(max_,area )
        return max_