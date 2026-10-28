# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dia = [0]
    
        def depth(node):
            if not node:
                return 0
            
            left_d = depth(node.left)
            right_d = depth(node.right)
            
            max_dia[0] = max(max_dia[0], left_d + right_d)
            return 1 + max(left_d, right_d)
        
        depth(root)
        return max_dia[0]