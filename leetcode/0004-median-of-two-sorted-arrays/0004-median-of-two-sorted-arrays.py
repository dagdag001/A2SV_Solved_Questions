class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def merge(n: List[int], m: List[int]):
            merged: List[int] = []
            l: int = 0
            r: int = 0
            while l < len(n) and  r < len(m):
                if n[l] < m[r]:
                    merged.append(n[l]) 
                    l+=1
                else:
                    merged.append(m[r]) 
                    r+=1
            while l < len(n):
                merged.append(n[l])
                l+=1
            while r < len(m):
                merged.append(m[r])
                r+=1
            return merged
        
        combined = merge(nums1, nums2)
        if len(combined) % 2 != 0:
            median =  combined[len(combined) // 2]
            return median
        else:
            median = (combined[len(combined) // 2] + combined[(len(combined) // 2) - 1] ) / 2
            return median


