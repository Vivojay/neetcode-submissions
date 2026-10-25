# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def trav(self, node, maxval):
        if node is None:
            return None
        if (maxval <= node.val):
            maxval = node.val
            self.goodcount += 1
        self.trav(node.left, maxval)
        self.trav(node.right, maxval)

    def goodNodes(self, root: TreeNode) -> int:
        maxval = root.val
        self.goodcount = 0
        self.trav(root, maxval)
        return self.goodcount
