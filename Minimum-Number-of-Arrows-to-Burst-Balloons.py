1class Solution:
2    def findMinArrowShots(self, points):
3        if not points:
4            return 0
5        points.sort(key=lambda x: x[1])
6        arrows = 1
7        arrow_pos = points[0][1]
8        for start, end in points[1:]:
9            if start > arrow_pos:
10                arrows += 1
11                arrow_pos = end
12        
13        return arrows