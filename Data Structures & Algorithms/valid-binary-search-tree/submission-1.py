# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def trav(self, node, lower=None, upper=None):
        if not node:
            return True

        if lower is not None and node.val <= lower:
            return False
        if upper is not None and node.val >= upper:
            return False

        l = self.trav(node.left, lower, node.val)
        r = self.trav(node.right, node.val, upper)
        return l and r

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.trav(root)


