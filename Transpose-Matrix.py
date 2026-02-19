class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        columns = len(matrix[0])
        res = [[0] * rows for i in range(len(matrix[0]))]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                res[c][r]  = matrix[r][c] 
        return res
