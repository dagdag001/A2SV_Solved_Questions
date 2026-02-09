1class Solution:
2    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
3        res = []
4        evenSum = sum(i for i in nums if i%2==0)
5        for val,idx in (queries):
6            if nums[idx] %2 == 0:
7                evenSum -= nums[idx]
8            nums[idx] += val
9            if nums[idx] %2 == 0:
10                 evenSum += nums[idx]
11            res.append(evenSum)
12        return res
13
14