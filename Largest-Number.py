1class Solution:
2    def largestNumber(self, nums: List[int]) -> str:
3        nums = list(map(str, nums))
4        nums.sort(key=lambda a:a*10, reverse= True)
5        return str(int("".join(nums)))