1class Solution:
2    def findCommonResponse(self, responses: List[List[str]]) -> str:
3        count = {}
4        for i in responses:
5            for j in set(i):
6                if j not in count:
7                    count[j] = 1
8                else:
9                    count[j] +=1
10        
11        return sorted(count.keys(), key=lambda x: (-count[x], x))[0]
12