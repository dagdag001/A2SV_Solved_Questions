class Solution:
    def subarraySum(self, nums, k):
        count = 0
        sum_ = 0
        freq = defaultdict(int)
        freq[0] = 1
        for n in nums:
            sum_ += n
            
            if sum_ - k in freq:
                count += freq[sum_ - k]

            freq[sum_] += 1

        return count