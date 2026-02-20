1class Solution:
2    def spiralOrder(self, matrix):
3        if not matrix or not matrix[0]:
4            return []
5        
6        result = []
7        top, bottom = 0, len(matrix) - 1
8        left, right = 0, len(matrix[0]) - 1
9        
10        while top <= bottom and left <= right:
11            for col in range(left, right + 1):
12                result.append(matrix[top][col])
13            top += 1
14            for row in range(top, bottom + 1):
15                result.append(matrix[row][right])
16            right -= 1
17            
18            if top <= bottom:
19                for col in range(right, left - 1, -1):
20                    result.append(matrix[bottom][col])
21                bottom -= 1
22            
23            if left <= right:
24                for row in range(bottom, top - 1, -1):
25                    result.append(matrix[row][left])
26                left += 1
27        
28        return result