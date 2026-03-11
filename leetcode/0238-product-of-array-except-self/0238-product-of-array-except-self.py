class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # before n
        prefix = 1
        ans = [0] * len(nums) 
        for n in range(len(nums)):
            ans[n] = prefix
            prefix*=nums[n]
        # after n
        suffix = 1
        for n in range(len(nums)-1, -1, -1):
            ans[n]*= suffix
            suffix *=nums[n]
        return ans
