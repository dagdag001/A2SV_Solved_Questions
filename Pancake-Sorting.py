1class Solution:
2    def pancakeSort(self, arr: List[int]) -> List[int]:
3        def flip(end):
4            start = 0
5            while start < end:
6                arr[start], arr[end] = arr[end], arr[start] 
7                start+=1
8                end-=1
9        n = len(arr)
10        res = []
11        for i in range(n-1, -1, -1):
12            max_idx = i
13            for j in range(i, -1, -1):
14                if arr[max_idx] < arr[j]:
15                    max_idx = j
16            if max_idx != i:
17                flip(max_idx)
18                flip(i)
19                res.append(max_idx + 1)
20                res.append(i+ 1)
21        return res