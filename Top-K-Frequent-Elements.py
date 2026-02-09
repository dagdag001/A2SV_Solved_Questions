1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        count= Counter(nums)
4        return [k for k, freq in count.most_common(k)]