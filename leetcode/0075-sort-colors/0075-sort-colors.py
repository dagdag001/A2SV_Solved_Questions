class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # bogo sort
        bucket1 =[]
        bucket2 =[]
        bucket3 =[]
        for num in nums:
            if num ==0:
                bucket1.append(num)
            elif num == 1:
                bucket2.append(num)
            else:
                bucket3.append(num)
        nums[:] = bucket1+bucket2+bucket3