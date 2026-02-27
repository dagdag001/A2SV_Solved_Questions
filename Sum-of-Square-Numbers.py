class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        low = 0
        high = c 
        ans = 0
        while low <= high:
            mid = low + (high-low)//2
            if mid * mid <= c:
                ans = mid 
                low = mid + 1 
            else:
                high = mid - 1 
        
        i = 0 
        j = ans 
        while i <= j:
            tmp = i*i + j*j 
            if tmp > c:
                j -= 1 
            elif tmp < c:
                i += 1
            else:
                return True 
        return False 