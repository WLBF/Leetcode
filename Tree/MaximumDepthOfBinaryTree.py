# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.depth = 0
        
    def dfs(self, node, dep):
        if node is not None:
            self.depth = max(self.depth, dep + 1)
            self.dfs(node.left, dep + 1)
            self.dfs(node.right, dep + 1)
        
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root, 0)
        return self.depth
