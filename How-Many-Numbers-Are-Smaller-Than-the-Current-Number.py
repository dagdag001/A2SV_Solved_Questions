from typing import List

class Solution:
	def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
		rank = {}
		sortNums = sorted(nums)
		for i, val in enumerate(sortNums):
			if val not in rank:
				rank[val] = i
		return [rank[x] for x in nums]