class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(nums[0])
        for i in range(1, len(nums)):
            current = TreeNode(nums[i])
            current.left = root
            parent = None
            if current.val >= root.val:
                root = current

            while current.left is not None and current.val < current.left.val:
                    temp = current.left.right
                    current.left.right = current
                    if parent is not None:
                        parent.right = current.left
                    parent = current.left
                    current.left = temp

        return root
