1from typing import List
2
3class Solution:
4    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
5        lookUp = {val: idx for idx, val in enumerate(list2)}
6        min_sum = float("inf")
7        result = []
8        
9        for i in range(len(list1)):
10            if list1[i] in lookUp:
11                s = i + lookUp[list1[i]]
12                
13                if s < min_sum:
14                    min_sum = s
15                    result = [list1[i]]
16                    
17                elif s == min_sum:
18                    result.append(list1[i])
19        
20        return result
21