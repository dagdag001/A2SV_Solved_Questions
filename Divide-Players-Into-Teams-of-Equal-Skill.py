1class Solution:
2    def dividePlayers(self, skill: List[int]) -> int:
3        skill.sort()
4        l = 0
5        r = len(skill) - 1
6        res = 0
7        team_sum = skill[l] + skill[r]
8
9        while l <= r:
10            chem = skill[l] + skill[r]
11            if chem != team_sum:
12                return -1
13            res+=(skill[l] * skill[r])
14            l+=1
15            r-=1
16        return res
17
18