1class Solution:
2    def majorityElement(self, nums: List[int]) -> List[int]:
3        n = len(nums)
4        count = Counter(nums)
5        res = []
6        for num, freq in count.items():
7            if freq > n // 3:
8                res.append(num)
9        return res
10