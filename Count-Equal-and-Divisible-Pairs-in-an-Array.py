1class Solution:
2    def countPairs(self, nums: List[int], k: int) -> int:
3        count = 0
4        for i in range(len(nums)-1):
5            for j in range(i+1 ,len(nums)):
6                if nums[i] == nums[j] and (i*j) % k == 0:
7                    count+=1
8        return count
9