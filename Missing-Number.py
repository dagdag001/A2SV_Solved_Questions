class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sumFirstNInteger =  (n*(n+1))//2
        return sumFirstNInteger- sum(nums)