class Solution:
    def imageSmoother(self, img):
        m, n = len(img), len(img[0])
        
        result = [[0] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                
                total = 0
                count = 0
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        if 0 <= i < m and 0 <= j < n:
                            total += img[i][j]
                            count += 1
                
                result[r][c] = total // count   
        
        return result