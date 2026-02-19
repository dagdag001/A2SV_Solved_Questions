1class Solution:
2    def countNegatives(self, grid: List[List[int]]) -> int:
3        neg =0
4        for row in grid:
5            for val in row:
6                if val < 0:
7                    neg +=1
8        return neg