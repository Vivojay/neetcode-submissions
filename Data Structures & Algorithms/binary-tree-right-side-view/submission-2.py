# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def traverse(self, node, level):
        if node is None: return None
        if level == len(self.ds):
            self.ds.append(node)
        self.traverse(node.right, level+1)
        self.traverse(node.left, level+1)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.ds = []
        self.traverse(root, 0);
        return [i.val for i in self.ds];


