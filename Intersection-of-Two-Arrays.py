1class Solution:
2    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        nums1_set = set(nums1)
4        nums2_set = set(nums2)
5        return list(nums1_set & nums2_set)