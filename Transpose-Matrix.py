1class Solution:
2    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
3        rows = len(matrix)
4        columns = len(matrix[0])
5        res = [[0] * rows for i in range(len(matrix[0]))]
6        for r in range(len(matrix)):
7            for c in range(len(matrix[0])):
8                res[c][r]  = matrix[r][c] 
9        return res
10