class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 2:
            return 0

        min_num = min(nums)
        max_num = max(nums)

        if min_num == max_num:
            return 0

        bucket_size = max(1, (max_num - min_num) // (n - 1))
        bucket_count = ((max_num - min_num) // bucket_size) + 1

        buckets = [[None, None] for _ in range(bucket_count)]

        for num in nums:
            idx = (num - min_num) // bucket_size

            if buckets[idx][0] is None:
                buckets[idx][0] = num
                buckets[idx][1] = num
            else:
                buckets[idx][0] = min(buckets[idx][0], num)
                buckets[idx][1] = max(buckets[idx][1], num)

        max_gap = 0
        prev_max = min_num

        for bucket in buckets:
            if bucket[0] is None:
                continue

            max_gap = max(max_gap, bucket[0] - prev_max)
            prev_max = bucket[1]

        return max_gap