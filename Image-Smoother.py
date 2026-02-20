1class Solution:
2    def imageSmoother(self, img):
3        m, n = len(img), len(img[0])
4        
5        result = [[0] * n for _ in range(m)]
6        
7        for r in range(m):
8            for c in range(n):
9                
10                total = 0
11                count = 0
12                for i in range(r - 1, r + 2):
13                    for j in range(c - 1, c + 2):
14                        
15                        if 0 <= i < m and 0 <= j < n:
16                            total += img[i][j]
17                            count += 1
18                
19                result[r][c] = total // count   
20        
21        return result