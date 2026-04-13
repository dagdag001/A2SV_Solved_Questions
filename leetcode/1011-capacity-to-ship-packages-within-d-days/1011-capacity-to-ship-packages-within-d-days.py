class Solution:
    def shipWithinDays(self, weights, days):
        def can_ship(cap):
            d = 1
            total = 0

            for w in weights:
                if total + w > cap:
                    d += 1
                    total = 0
                total += w

            return d <= days

        left, right = max(weights), sum(weights)

        while left <= right:
            mid = (left + right) // 2
            if can_ship(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left