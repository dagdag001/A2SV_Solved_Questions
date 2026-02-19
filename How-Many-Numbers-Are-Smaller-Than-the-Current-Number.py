1class Solution:
2    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
3        rank = {}
4        sortNums = sorted(nums)
5        for i, val in enumerate(sortNums):
6            if val not in rank:
7                rank[val] = i
8
9        return [rank[x] for x in nums]
10
11