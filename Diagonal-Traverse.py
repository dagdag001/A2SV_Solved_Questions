1class Solution:
2    def findDiagonalOrder(self, mat):
3        if not mat or not mat[0]:
4            return []
5        
6        m, n = len(mat), len(mat[0])
7        diagonals = {}
8        
9        for r in range(m):
10            for c in range(n):
11                if r + c not in diagonals:
12                    diagonals[r + c] = []
13                diagonals[r + c].append(mat[r][c])
14        
15        result = []
16        
17        for d in range(m + n - 1):
18            if d % 2 == 0:
19                result.extend(diagonals[d][::-1])  
20            else:
21                result.extend(diagonals[d])
22        
23        return result