class Solution:
    def spiralMatrixIII(self, rows, cols, rStart, cStart):
        
        result = []
        total = rows * cols
        
        # Directions: East, South, West, North
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        
        r, c = rStart, cStart
        result.append([r, c])
        
        steps = 1  
        d = 0      
        while len(result) < total:
            
            for _ in range(2):
                
                dr, dc = directions[d]
                
                for _ in range(steps):
                    r += dr
                    c += dc
                    
                    if 0 <= r < rows and 0 <= c < cols:
                        result.append([r, c])
                
                d = (d + 1) % 4
            
            steps += 1
        
        return result