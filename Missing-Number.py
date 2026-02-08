1class Solution:
2    def missingNumber(self, nums: List[int]) -> int:
3        n = len(nums)
4        sumFirstNInteger =  (n*(n+1))//2
5        return sumFirstNInteger- sum(nums)