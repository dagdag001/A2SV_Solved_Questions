1class Solution:
2    def separateDigits(self, nums: List[int]) -> List[int]:
3        def separate(num):
4            res = []
5            while num > 0:
6                res.append(num % 10)
7                num //= 10
8            return res[::-1]
9        res = []
10        for i in nums:
11            res.extend(separate(i))
12        return res
13             
14
15
16