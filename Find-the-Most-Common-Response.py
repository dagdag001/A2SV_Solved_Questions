class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        count = {}
        for i in responses:
            for j in set(i):
                if j not in count:
                    count[j] = 1
                else:
                    count[j] +=1
        
        return sorted(count.keys(), key=lambda x: (-count[x], x))[0]
