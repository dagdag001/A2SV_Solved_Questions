class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        # left side
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r ) // 2
            if nums[mid] >= target:
                r = mid -1
            else:
                l = mid +1
        start = -1
        if l < len(nums) and nums[l] == target:
            start = l
        else:
            return [-1, -1] 
        
        # right side
        l = 0
        r = len(nums) - 1
        end =-1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= target:
                l = mid +1
            else:
                r = mid - 1
        
        if nums[r] == target:
            end = r
        return [start, end] 
                