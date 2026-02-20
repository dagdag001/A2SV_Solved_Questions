1class Solution:
2    def flipAndInvertImage(self, image):
3        n = len(image)
4        result = []
5        
6        for i in range(n):
7            new_row = []
8            
9            # Flip
10            for j in range(n - 1, -1, -1):
11                
12                # Invert
13                if image[i][j] == 0:
14                    new_row.append(1)
15                else:
16                    new_row.append(0)
17            
18            result.append(new_row)
19        
20        return result