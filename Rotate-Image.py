1class Solution:
2    def rotate(self, matrix: List[List[int]]) -> None:
3        """
4        Do not return anything, modify matrix in-place instead.
5        """
6        # TRANSPOSE then REVERSE THE ROW
7        row = len(matrix)
8        for i in range(row):
9            for j in range(i+1, row):
10                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
11        for i in (matrix):
12            i.reverse()
13