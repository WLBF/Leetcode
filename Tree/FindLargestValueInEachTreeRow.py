# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.ans = []

    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.dfs(root, 0)
        return self.ans


    def dfs(self, node, level):
        if not node:
            return

        if level >= len(self.ans):
            self.ans.append(node.val)
        else:
            self.ans[level] = max(self.ans[level], node.val)
    
        self.dfs(node.left, level + 1)
        self.dfs(node.right, level + 1)
