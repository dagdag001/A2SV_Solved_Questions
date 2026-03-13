class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        total = 0
        def difference_sort(x):
            return x[0] - x[1]
        costs.sort(key=difference_sort)
        for i in range(len(costs)//2):
            total += costs[i][0]
        for i in range(len(costs)//2, len(costs)):
            total += costs[i][1]
        return total
