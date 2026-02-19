1class Solution:
2    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
3        ans=defaultdict(list)
4
5        for file in paths:
6            splited = file.split(" ")
7            directory=splited[0]
8
9            for i in splited[1:]:
10                name,content=i.split("(")
11                content=content[:-1]
12
13                full_path= f"{directory}/{name}"
14                ans[content].append(full_path)
15
16            
17        return [val for key,val in ans.items() if len(val)>1]