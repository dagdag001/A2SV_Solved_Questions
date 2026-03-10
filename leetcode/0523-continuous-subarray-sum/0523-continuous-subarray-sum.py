class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        remainder = {0: -1}
        tot = 0
        for i, n in enumerate(nums):
            tot +=n
            if (tot % k) not in remainder:
                remainder[tot % k] = i 
            elif i - remainder[tot % k] > 1:
                return True
        return False

