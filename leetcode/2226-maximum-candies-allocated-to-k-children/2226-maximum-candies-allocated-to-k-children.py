class Solution:
    def maximumCandies(self, candies, k):
        def can_allocate(x):
            return sum(c // x for c in candies) >= k

        left, right = 1, max(candies)
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if can_allocate(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans