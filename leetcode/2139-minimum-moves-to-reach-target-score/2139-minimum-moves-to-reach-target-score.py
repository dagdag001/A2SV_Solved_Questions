class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        inc = 0
        double = 0
        for i in range(maxDoubles):
            if target <= 1:
                break
            if target % 2 != 0:
                target -=1
                inc +=1
            double +=1
            target //= 2
        inc += target - 1
        return inc+ double 
            