# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ctr = 0
        stack = []
        current = root

        while (current or stack):
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            ctr += 1

            if ctr == k:
                return current.val

            current = current.right

        return current.val
