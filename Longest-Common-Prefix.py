1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        def common_prefix(n,m):
4            length = 0
5            for i in range(len(n)):
6                if (i == len(m)):
7                    break
8                if n[i] == m[i]:
9                    length +=1
10                else:
11                    break
12                
13            return n[:length:]
14        common = strs[0]
15        for i in range(len(strs)-1):
16            common = common_prefix(common,strs[i+1])
17            if common == "":
18                return ""
19        return common