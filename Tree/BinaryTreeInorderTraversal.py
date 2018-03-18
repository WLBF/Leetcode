# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        valueList = []
        self.traversal(root, valueList)
        return valueList

    def traversal(self, node, valueList):
        if node is not None:
            self.traversal(node.left, valueList)
            valueList.append(node.val)
            self.traversal(node.right, valueList)
