class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def common_prefix(n,m):
            length = 0
            for i in range(len(n)):
                if (i == len(m)):
                   break
                if n[i] == m[i]:
                    length +=1
                else:
                    break
                
            return n[:length:]
        common = strs[0]
        for i in range(len(strs)-1):
            common = common_prefix(common,strs[i+1])
            if common == "":
                return ""
        return common