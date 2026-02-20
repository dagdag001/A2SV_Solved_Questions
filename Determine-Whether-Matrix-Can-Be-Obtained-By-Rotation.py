1class Solution:
2    def findRotation(self, mat, target):
3        
4        for _ in range(4):
5            if mat == target:
6                return True
7            mat = [list(row) for row in zip(*mat[::-1])]
8        
9        return False