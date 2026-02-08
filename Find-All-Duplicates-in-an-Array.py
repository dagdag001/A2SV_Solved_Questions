1class Solution:
2    def findDuplicates(self, nums: List[int]) -> List[int]:
3        count = Counter(nums)
4        res = []
5        for i, freq in count.items():
6            if freq > 1:
7                res.append(i)
8        return res