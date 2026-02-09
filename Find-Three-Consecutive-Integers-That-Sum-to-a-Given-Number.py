class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        # x + x+1 + x+ 2 => 3x + 3 = num 
        # x = (num - 3) / 3 
        x = (num - 3) / 3
        if x.is_integer():
            x = int(x)
            return [x, x+1, x+2]
        else:
            return []
       