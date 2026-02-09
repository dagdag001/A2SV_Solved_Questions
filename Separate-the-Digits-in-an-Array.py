class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        def separate(num):
            res = []
            while num > 0:
                res.append(num % 10)
                num //= 10
            return res[::-1]
        res = []
        for i in nums:
            res.extend(separate(i))
        return res
             
