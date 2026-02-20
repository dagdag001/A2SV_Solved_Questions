1class Solution:
2    def spiralMatrixIII(self, rows, cols, rStart, cStart):
3        
4        result = []
5        total = rows * cols
6        
7        # Directions: East, South, West, North
8        directions = [(0,1), (1,0), (0,-1), (-1,0)]
9        
10        r, c = rStart, cStart
11        result.append([r, c])
12        
13        steps = 1  
14        d = 0      
15        while len(result) < total:
16            
17            for _ in range(2):
18                
19                dr, dc = directions[d]
20                
21                for _ in range(steps):
22                    r += dr
23                    c += dc
24                    
25                    if 0 <= r < rows and 0 <= c < cols:
26                        result.append([r, c])
27                
28                d = (d + 1) % 4
29            
30            steps += 1
31        
32        return result