class Solution:
    def flipAndInvertImage(self, image):
        n = len(image)
        result = []
        
        for i in range(n):
            new_row = []
            
            # Flip
            for j in range(n - 1, -1, -1):
                
                # Invert
                if image[i][j] == 0:
                    new_row.append(1)
                else:
                    new_row.append(0)
            
            result.append(new_row)
        
        return result