class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count= Counter(nums)
        return [k for k, freq in count.most_common(k)]