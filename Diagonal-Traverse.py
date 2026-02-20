class Solution:
    def findDiagonalOrder(self, mat):
        if not mat or not mat[0]:
            return []
        
        m, n = len(mat), len(mat[0])
        diagonals = {}
        
        for r in range(m):
            for c in range(n):
                if r + c not in diagonals:
                    diagonals[r + c] = []
                diagonals[r + c].append(mat[r][c])
        
        result = []
        
        for d in range(m + n - 1):
            if d % 2 == 0:
                result.extend(diagonals[d][::-1])  
            else:
                result.extend(diagonals[d])
        
        return result