# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def balancedTree(root):
            if not root: 
                return [True, 0]

            left_tree = balancedTree(root.left)
            right_tree = balancedTree(root.right)

            if left_tree[0] and right_tree[0] and abs(left_tree[1] - right_tree[1]) <= 1:
                return [True, 1 + max(left_tree[1], right_tree[1])]
            else:
                return [False, 1 + max(left_tree[1], right_tree[1])]


        return balancedTree(root)[0]