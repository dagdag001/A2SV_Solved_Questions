class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        lookUp = {val: idx for idx, val in enumerate(list2)}
        min_sum = float("inf")
        result = []
        
        for i in range(len(list1)):
            if list1[i] in lookUp:
                s = i + lookUp[list1[i]]
                
                if s < min_sum:
                    min_sum = s
                    result = [list1[i]]
                    
                elif s == min_sum:
                    result.append(list1[i])
        
        return result
