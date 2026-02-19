class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg =0
        for row in grid:
            for val in row:
                if val < 0:
                    neg +=1
        return neg