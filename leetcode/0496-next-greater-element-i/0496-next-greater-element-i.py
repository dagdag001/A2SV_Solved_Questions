class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        nxt = {}

        for n in nums2:
            while stack and n > stack[-1]:
                nxt[stack.pop()] = n
            stack.append(n)

        for n in stack:
            nxt[n] = -1

        return [nxt[x] for x in nums1]