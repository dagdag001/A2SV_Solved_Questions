class Solution:
    def minStoneSum(self, piles, k):
        heap = [-x for x in piles]
        heapq.heapify(heap)

        for _ in range(k):
            x = -heapq.heappop(heap)
            x = x - x // 2
            heapq.heappush(heap, -x)

        return -sum(heap)