class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 0
        r = len(skill) - 1
        res = 0
        team_sum = skill[l] + skill[r]

        while l <= r:
            chem = skill[l] + skill[r]
            if chem != team_sum:
                return -1
            res+=(skill[l] * skill[r])
            l+=1
            r-=1
        return res

