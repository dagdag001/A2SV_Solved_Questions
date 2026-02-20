1class Solution:
2    def setZeroes(self, matrix: List[List[int]]) -> None:
3        """
4        Do not return anything, modify matrix in-place instead.
5        """
6        rows = len(matrix)
7        cols = len(matrix[0])
8        
9        first_row_zero = False
10        first_col_zero = False
11        
12        for j in range(cols):
13            if matrix[0][j] == 0:
14                first_row_zero = True
15                break
16        
17        for i in range(rows):
18            if matrix[i][0] == 0:
19                first_col_zero = True
20                break
21        
22        for i in range(1, rows):
23            for j in range(1, cols):
24                if matrix[i][j] == 0:
25                    matrix[i][0] = 0
26                    matrix[0][j] = 0
27        
28        for i in range(1, rows):
29            for j in range(1, cols):
30                if matrix[i][0] == 0 or matrix[0][j] == 0:
31                    matrix[i][j] = 0
32        
33        if first_row_zero:
34            for j in range(cols):
35                matrix[0][j] = 0
36        
37        if first_col_zero:
38            for i in range(rows):
39                matrix[i][0] = 0
40        