class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []
        for i, freq in count.items():
            if freq > 1:
                res.append(i)
        return res