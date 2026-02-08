1class Solution:
2    def removeComments(self, source):
3        result = []
4        in_block = False
5        current = ""
6
7        for line in source:
8            i = 0
9
10            while i < len(line):
11                if not in_block and i + 1 < len(line) and line[i:i+2] == "/*":
12                    in_block = True
13                    i += 2
14                elif in_block and i + 1 < len(line) and line[i:i+2] == "*/":
15                    in_block = False
16                    i += 2
17                elif not in_block and i + 1 < len(line) and line[i:i+2] == "//":
18                    break
19                elif not in_block:
20                    current += line[i]
21                    i += 1
22
23                else:
24                    i += 1
25            if not in_block and current:
26                result.append(current)
27                current = ""
28
29        return result
30