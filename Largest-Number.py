class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        nums.sort(key=lambda a:a*10, reverse= True)
        return str(int("".join(nums)))