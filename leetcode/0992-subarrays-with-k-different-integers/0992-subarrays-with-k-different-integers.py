class Solution:
    def subarraysWithKDistinct(self, nums, k):
        count = defaultdict(int)
        res = 0
        lf = 0
        ln = 0
        for r in range(len(nums)):
            count[nums[r]] += 1
            while len(count) > k:
                count[nums[ln]] -=1
                if count[nums[ln]] == 0:
                    count.pop(nums[ln])
                ln+=1
                lf = ln
            while count[nums[ln]] > 1:
                count[nums[ln]] -=1
                ln +=1
            if len(count) == k:
                res += ln - lf + 1
        return res