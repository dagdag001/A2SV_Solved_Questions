# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        def dfs(node, current_sum):
            if not node:
                return 0
            count = 1 if node.val == current_sum else 0
            count += dfs(node.left, current_sum - node.val)
            count += dfs(node.right, current_sum - node.val)
            return count
        
        return dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)