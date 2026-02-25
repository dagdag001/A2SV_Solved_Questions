1class Solution:
2    def numRescueBoats(self, people: List[int], limit: int) -> int:
3        people.sort()
4        boat = 0
5        l = 0 
6        r = len(people) - 1 
7        while l <= r :
8            if people[l] + people[r] <= limit:
9                l+=1
10            r-=1
11            boat+=1
12        return boat
13            
14
15                
16