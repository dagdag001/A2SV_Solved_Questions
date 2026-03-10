class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_ = 0
        res = []
        for num in nums:
            sum_ +=num
            res.append(sum_)
        return res