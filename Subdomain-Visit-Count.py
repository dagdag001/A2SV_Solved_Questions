1class Solution:
2    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
3        res = []
4        all_domains = defaultdict(int)
5        for s in cpdomains:
6            arr = s.split()
7            visited = int(arr[0])
8            path = arr[1].split(".")
9            for i in range(len(path)):
10                domain = ".".join(path[i:])
11                if domain in all_domains:
12                    all_domains[domain] += visited
13                else: 
14                    all_domains[domain] = visited
15
16        for key, val in all_domains.items():
17            temp = str(val) + " " + key
18            res.append(temp)
19
20        return res
21         