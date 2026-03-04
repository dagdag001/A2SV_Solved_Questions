class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        i = 1
        while True:
            sum_ = i 
            Found = True
            for j in nums:
                sum_ +=j
                if sum_ < 1:
                    Found = False
                    break
            if Found:
                return i
            else:
                i+=1
                

